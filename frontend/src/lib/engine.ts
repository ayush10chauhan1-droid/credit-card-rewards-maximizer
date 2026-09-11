// =====================================================================
// 🧮 SWIPESMART AI — CLIENT CALCULATION & API ENGINE
// 0ms Latency Instant Math with FastAPI Synchronous/Async Integration
// =====================================================================

import { CARDS_DATABASE, CreditCardData } from './data';

const API_BASE_URL = 'http://localhost:8000';

export interface CompareResult {
  card: string;
  bank: string;
  rate: number;
  reward: number;
  source: string;
  cap_note: string | null;
  type: string;
  tier: string;
  network: string;
  annual_fee: number;
  fee_waiver_spend: number;
  break_even_spend: number;
  forex_markup: number;
  domestic_lounges: string;
  summary: string;
  apply_url: string;
}

export interface SinglePurchaseResponse {
  results: CompareResult[];
  best_card: string | null;
  best_reward: number;
  runner_up: string | null;
  runner_up_card?: CompareResult | null;
  savings_delta: number;
  tips: Array<{ icon: string; title: string; text: string }>;
  ai_rationale?: string;
}

export interface CategoryAssignment {
  spend: number;
  assigned_card: string;
  effective_rate: number;
  monthly_reward: number;
  yearly_reward: number;
  source: string;
  cap_note: string | null;
  all_options: Array<{ card: string; rate: number; reward: number; source: string }>;
}

export interface WalletStrategyResponse {
  category_assignments: Record<string, CategoryAssignment>;
  total_optimized_monthly_reward: number;
  total_optimized_yearly_reward: number;
  net_optimized_yearly_return: number;
  optimized_roi_pct: number;
  best_single_card: { card: string; net_yearly: number };
  synergy_vs_single: number;
  total_annual_fees: number;
  total_effective_fees: number;
  card_fee_details: Array<{ card: string; base_fee: number; effective_fee: number; waived: boolean; waiver_spend_target: number; routed_spend: number }>;
  card_usage_distribution: Record<string, { spend: number; reward: number; categories: string[] }>;
  ai_summary?: string;
  error?: string;
}

export interface SpendGap {
  category: string;
  monthly_spend: number;
  current_rate: number;
  current_card: string;
  potential_rate: number;
  annual_leak_estimate: number;
  urgency: 'High' | 'Medium';
}

export interface CardRecommendation {
  card: string;
  bank: string;
  tier: string;
  type: string;
  annual_fee: number;
  domestic_lounges: string;
  incremental_annual_profit: number;
  conquered_categories: Array<{ category: string; new_rate: number }>;
  apply_url: string;
  summary: string;
}

// ---------------------------------------------------------------------
// Client-side instant calculation functions (Exact Python logic mirror)
// ---------------------------------------------------------------------

export function getRewardRate(cardName: string, category: string, vendor?: string | null): [number, string] {
  const card = CARDS_DATABASE[cardName];
  if (!card) return [0.0, "Unknown Card"];

  if (vendor && card.vendor_rewards && vendor in card.vendor_rewards) {
    return [card.vendor_rewards[vendor], `🏪 ${vendor} Partner Rate`];
  }

  if (card.rewards && category in card.rewards) {
    return [card.rewards[category], `📂 ${category}`];
  }

  const other = card.rewards ? (card.rewards["Other"] || 1.0) : 1.0;
  return [other, "📂 Standard Spend Rate"];
}

export function getPointMultiplier(card: CreditCardData, valuationMode: string = "default"): number {
  if (card.type === "cashback") return 1.00;
  if (card.point_valuation && valuationMode in card.point_valuation) {
    return card.point_valuation[valuationMode];
  }
  return card.point_valuation?.default || 1.00;
}

export function applyMonthlyCap(cardName: string, category: string, vendor: string | null | undefined, rawReward: number): [number, string | null] {
  const card = CARDS_DATABASE[cardName];
  if (!card) return [rawReward, null];
  const caps = card.caps || {};

  if (cardName === "SBI Cashback Card") {
    const onlineCap = caps.online_monthly_cashback || 5000;
    if (rawReward > onlineCap) return [onlineCap, `Capped at ₹${onlineCap.toLocaleString()}/mo on 5% online spends`];
  } else if (cardName === "Swiggy HDFC") {
    if (vendor === "Swiggy" || category === "Dining") {
      const swiggyCap = caps.swiggy_monthly_cashback || 1500;
      if (rawReward > swiggyCap) return [swiggyCap, `Capped at ₹${swiggyCap.toLocaleString()}/mo on Swiggy`];
    } else if (category === "Online Shopping" || category === "Grocery") {
      const onlineCap = caps.online_monthly_cashback || 1500;
      if (rawReward > onlineCap) return [onlineCap, `Capped at ₹${onlineCap.toLocaleString()}/mo on 5% merchants`];
    }
  } else if (cardName === "HDFC Millennia") {
    const pCap = caps.partner_monthly_cashback || 1000;
    if (rawReward > pCap) return [pCap, `Capped at ₹${pCap.toLocaleString()}/mo on 5% partner spends`];
  } else if (cardName === "Axis Ace") {
    if (category === "Utilities") {
      const uCap = caps.utility_monthly_cashback || 500;
      if (rawReward > uCap) return [uCap, `Capped at ₹${uCap.toLocaleString()}/mo on Google Pay utilities`];
    } else if (category === "Dining") {
      const dCap = caps.dining_monthly_cashback || 500;
      if (rawReward > dCap) return [dCap, `Capped at ₹${dCap.toLocaleString()}/mo on Swiggy/Zomato`];
    }
  } else if (cardName === "Airtel Axis") {
    if (vendor === "Airtel Mobile/Broadband") {
      const aCap = caps.airtel_monthly_cashback || 250;
      if (rawReward > aCap) return [aCap, `Capped at ₹${aCap.toLocaleString()}/mo on Airtel bills`];
    } else if (category === "Utilities") {
      const uCap = caps.utility_monthly_cashback || 250;
      if (rawReward > uCap) return [uCap, `Capped at ₹${uCap.toLocaleString()}/mo on utility bills`];
    } else if (category === "Dining" || category === "Grocery") {
      const fCap = caps.food_grocery_monthly_cashback || 500;
      if (rawReward > fCap) return [fCap, `Capped at ₹${fCap.toLocaleString()}/mo on food & grocery`];
    }
  } else if (cardName === "SBI BPCL Octane" && category === "Fuel") {
    const fuelCap = (caps.fuel_monthly_points || 2500) * 0.25;
    if (rawReward > fuelCap) return [fuelCap, `Capped at ₹${fuelCap.toLocaleString()}/mo on BPCL fuel`];
  }

  return [rawReward, null];
}

export function compareCardsClient(
  cardNames: string[],
  category: string,
  amount: number,
  vendor?: string | null,
  valuationMode: string = "default"
): SinglePurchaseResponse {
  const results: CompareResult[] = [];

  for (const name of cardNames) {
    const cardInfo = CARDS_DATABASE[name];
    if (!cardInfo) continue;

    const [rate, source] = getRewardRate(name, category, vendor);
    const rawReward = Math.round(amount * (rate / 100.0) * 100) / 100;
    const multiplier = getPointMultiplier(cardInfo, valuationMode);
    const rewardInr = Math.round(rawReward * multiplier * 100) / 100;
    const [cappedReward, capNote] = applyMonthlyCap(name, category, vendor, rewardInr);

    const fee = cardInfo.annual_fee || 0;
    const breakEven = (fee > 0 && rate > 0) ? Math.round(fee / ((rate * multiplier) / 100.0)) : 0;

    results.push({
      card: name,
      bank: cardInfo.bank,
      rate,
      reward: cappedReward,
      source,
      cap_note: capNote,
      type: cardInfo.type,
      tier: cardInfo.tier,
      network: cardInfo.network,
      annual_fee: fee,
      fee_waiver_spend: cardInfo.fee_waiver_spend || 0,
      break_even_spend: breakEven,
      forex_markup: cardInfo.forex_markup,
      domestic_lounges: cardInfo.domestic_lounges,
      summary: cardInfo.summary,
      apply_url: cardInfo.apply_url
    });
  }

  results.sort((a, b) => b.reward - a.reward || a.annual_fee - b.annual_fee);
  const best = results[0] || null;
  const runnerUp = results[1] || null;
  const bestReward = best ? best.reward : 0;
  const runnerUpReward = runnerUp ? runnerUp.reward : 0;
  const savingsDelta = Math.round((bestReward - runnerUpReward) * 100) / 100;

  // Generate smart tips
  const tips: Array<{ icon: string; title: string; text: string }> = [];
  if (best) {
    if (best.cap_note) {
      tips.push({ icon: "⚠️", title: "Monthly Spend Cap Notice", text: best.cap_note });
    }
    if (best.annual_fee > 0 && best.break_even_spend > 0) {
      tips.push({
        icon: "⚖️",
        title: "Fee Break-Even Spend",
        text: `Spend ₹${best.break_even_spend.toLocaleString()} annually on this card to fully offset its ₹${best.annual_fee.toLocaleString()} annual fee purely from rewards.`
      });
    }
    if (runnerUp && savingsDelta > 0) {
      tips.push({
        icon: "💡",
        title: `₹${savingsDelta.toLocaleString()} Advantage vs #${runnerUp.card}`,
        text: `Swiping ${best.card} yields ₹${savingsDelta.toFixed(2)} more on this transaction than your next best alternative.`
      });
    }
  }

  return {
    results,
    best_card: best ? best.card : null,
    best_reward: bestReward,
    runner_up: runnerUp ? runnerUp.card : null,
    runner_up_card: runnerUp,
    savings_delta: savingsDelta,
    tips
  };
}

export function findOptimalWalletStrategyClient(
  walletCards: string[],
  monthlySpend: Record<string, number>,
  valuationMode: string = "default"
): WalletStrategyResponse {
  const validCards = walletCards.filter(c => c in CARDS_DATABASE);
  if (validCards.length === 0) {
    return {
      category_assignments: {},
      total_optimized_monthly_reward: 0,
      total_optimized_yearly_reward: 0,
      net_optimized_yearly_return: 0,
      optimized_roi_pct: 0,
      best_single_card: { card: "None", net_yearly: 0 },
      synergy_vs_single: 0,
      total_annual_fees: 0,
      total_effective_fees: 0,
      card_fee_details: [],
      card_usage_distribution: {},
      error: "Please select at least one valid card in your wallet."
    };
  }

  const categoryAssignments: Record<string, CategoryAssignment> = {};
  let totalMonthlyReward = 0;
  const usageDist: Record<string, { spend: number; reward: number; categories: string[] }> = {};
  for (const c of validCards) usageDist[c] = { spend: 0, reward: 0, categories: [] };

  for (const [category, spend] of Object.entries(monthlySpend)) {
    if (spend <= 0) continue;

    let bestCard = validCards[0];
    let highestReward = -1;
    let bestRate = 0;
    let bestSource = "";
    let bestCapNote: string | null = null;
    const options: Array<{ card: string; rate: number; reward: number; source: string }> = [];

    for (const cardName of validCards) {
      const card = CARDS_DATABASE[cardName];
      const mult = getPointMultiplier(card, valuationMode);
      const [rate, source] = getRewardRate(cardName, category);
      const rawReward = (spend * (rate / 100.0)) * mult;
      const [cappedReward, capNote] = applyMonthlyCap(cardName, category, null, rawReward);

      options.push({ card: cardName, rate, reward: Math.round(cappedReward * 100) / 100, source });

      if (cappedReward > highestReward) {
        highestReward = cappedReward;
        bestCard = cardName;
        bestRate = rate;
        bestSource = source;
        bestCapNote = capNote;
      }
    }

    options.sort((a, b) => b.reward - a.reward);

    categoryAssignments[category] = {
      spend,
      assigned_card: bestCard,
      effective_rate: bestRate,
      monthly_reward: Math.round(highestReward * 100) / 100,
      yearly_reward: Math.round(highestReward * 12 * 100) / 100,
      source: bestSource,
      cap_note: bestCapNote,
      all_options: options
    };

    totalMonthlyReward += highestReward;
    if (usageDist[bestCard]) {
      usageDist[bestCard].spend += spend;
      usageDist[bestCard].reward += highestReward;
      usageDist[bestCard].categories.push(category);
    }
  }

  const yearlyGrossReward = totalMonthlyReward * 12;

  // Fee waivers
  let totalFees = 0;
  let effectiveFees = 0;
  const cardFeeDetails: Array<{ card: string; base_fee: number; effective_fee: number; waived: boolean; waiver_spend_target: number; routed_spend: number }> = [];

  for (const c of validCards) {
    const info = CARDS_DATABASE[c];
    const fee = info.annual_fee || 0;
    const waiverTarget = info.fee_waiver_spend || 0;
    const routedAnnual = (usageDist[c]?.spend || 0) * 12;
    const isWaived = waiverTarget > 0 && routedAnnual >= waiverTarget;
    const eff = isWaived ? 0 : fee;

    totalFees += fee;
    effectiveFees += eff;
    cardFeeDetails.push({
      card: c,
      base_fee: fee,
      effective_fee: eff,
      waived: isWaived,
      waiver_spend_target: waiverTarget,
      routed_spend: routedAnnual
    });
  }

  const netYearly = Math.round((yearlyGrossReward - effectiveFees) * 100) / 100;
  const totalMonthlySpend = Object.values(monthlySpend).reduce((a, b) => a + b, 0);
  const totalAnnualSpend = totalMonthlySpend * 12;
  const roiPct = totalAnnualSpend > 0 ? Math.round((netYearly / totalAnnualSpend) * 10000) / 100 : 0;

  // Best single card comparison benchmark
  let bestSingleCard = validCards[0];
  let bestSingleReturn = -999999;
  for (const c of validCards) {
    let singleCardMonthlyReward = 0;
    const cInfo = CARDS_DATABASE[c];
    const mult = getPointMultiplier(cInfo, valuationMode);
    for (const [cat, sp] of Object.entries(monthlySpend)) {
      const [rt] = getRewardRate(c, cat);
      const raw = (sp * (rt / 100.0)) * mult;
      const [cap] = applyMonthlyCap(c, cat, null, raw);
      singleCardMonthlyReward += cap;
    }
    const annualFee = cInfo.annual_fee || 0;
    const waiverTarget = cInfo.fee_waiver_spend || 0;
    const waived = waiverTarget > 0 && totalAnnualSpend >= waiverTarget;
    const netSingle = (singleCardMonthlyReward * 12) - (waived ? 0 : annualFee);
    if (netSingle > bestSingleReturn) {
      bestSingleReturn = netSingle;
      bestSingleCard = c;
    }
  }

  const synergy = Math.max(0, Math.round((netYearly - bestSingleReturn) * 100) / 100);

  return {
    category_assignments: categoryAssignments,
    total_optimized_monthly_reward: Math.round(totalMonthlyReward * 100) / 100,
    total_optimized_yearly_reward: Math.round(yearlyGrossReward * 100) / 100,
    net_optimized_yearly_return: netYearly,
    optimized_roi_pct: roiPct,
    best_single_card: { card: bestSingleCard, net_yearly: Math.round(bestSingleReturn) },
    synergy_vs_single: synergy,
    total_annual_fees: totalFees,
    total_effective_fees: effectiveFees,
    card_fee_details: cardFeeDetails,
    card_usage_distribution: usageDist
  };
}

export function analyzeSpendGapsClient(walletCards: string[], monthlySpend: Record<string, number>): SpendGap[] {
  const strategy = findOptimalWalletStrategyClient(walletCards, monthlySpend);
  if (strategy.error) return [];

  const gaps: SpendGap[] = [];
  for (const [cat, data] of Object.entries(strategy.category_assignments)) {
    if (data.spend >= 3000 && data.effective_rate < 2.5) {
      const annualLeak = Math.round(data.spend * 12 * (0.05 - (data.effective_rate / 100.0)));
      gaps.push({
        category: cat,
        monthly_spend: data.spend,
        current_rate: data.effective_rate,
        current_card: data.assigned_card,
        potential_rate: 5.0,
        annual_leak_estimate: Math.max(0, annualLeak),
        urgency: data.spend >= 10000 ? 'High' : 'Medium'
      });
    }
  }
  gaps.sort((a, b) => b.annual_leak_estimate - a.annual_leak_estimate);
  return gaps;
}

export function recommendNextCardsClient(
  currentWallet: string[],
  monthlySpend: Record<string, number>,
  lifestyleFilter: string = "All",
  maxFee?: number | null
): CardRecommendation[] {
  const currentStrategy = findOptimalWalletStrategyClient(currentWallet, monthlySpend);
  const currentNet = currentStrategy.net_optimized_yearly_return || 0;
  const candidates: CardRecommendation[] = [];

  for (const [cardName, cardInfo] of Object.entries(CARDS_DATABASE)) {
    if (currentWallet.includes(cardName)) continue;
    const fee = cardInfo.annual_fee || 0;
    if (maxFee !== undefined && maxFee !== null && fee > maxFee) continue;

    if (lifestyleFilter === "Lifetime Free" && fee > 0) continue;
    if (lifestyleFilter === "Pure Cashback" && cardInfo.type !== "cashback") continue;
    if (lifestyleFilter === "Travel & Lounges" && !cardInfo.tier.includes("Travel") && !cardInfo.tier.includes("Super Premium") && cardInfo.domestic_lounges === "None") continue;
    if (lifestyleFilter === "Super Premium" && !cardInfo.tier.includes("Super Premium")) continue;

    const simulatedWallet = [...currentWallet, cardName];
    const simStrategy = findOptimalWalletStrategyClient(simulatedWallet, monthlySpend);
    if (simStrategy.error) continue;

    const newNet = simStrategy.net_optimized_yearly_return;
    const incProfit = Math.round((newNet - currentNet) * 100) / 100;

    const conquered: Array<{ category: string; new_rate: number }> = [];
    for (const [cat, assign] of Object.entries(simStrategy.category_assignments)) {
      if (assign.assigned_card === cardName) {
        conquered.push({ category: cat, new_rate: assign.effective_rate });
      }
    }

    if (incProfit > 0 || fee === 0) {
      candidates.push({
        card: cardName,
        bank: cardInfo.bank,
        tier: cardInfo.tier,
        type: cardInfo.type,
        annual_fee: fee,
        domestic_lounges: cardInfo.domestic_lounges,
        incremental_annual_profit: incProfit,
        conquered_categories: conquered,
        apply_url: cardInfo.apply_url,
        summary: cardInfo.summary
      });
    }
  }

  candidates.sort((a, b) => b.incremental_annual_profit - a.incremental_annual_profit);
  return candidates;
}

// ---------------------------------------------------------------------
// Server API fetchers (with graceful fallback to client math)
// ---------------------------------------------------------------------
export async function fetchCompareAPI(
  cards: string[],
  category: string,
  amount: number,
  vendor?: string | null,
  valuationMode: string = "default"
): Promise<SinglePurchaseResponse> {
  try {
    const res = await fetch(`${API_BASE_URL}/api/compare`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ cards, category, amount, vendor, valuation_mode: valuationMode, include_ai: true })
    });
    if (res.ok) {
      return await res.json();
    }
  } catch {
    // Graceful fallback to client math
  }
  return compareCardsClient(cards, category, amount, vendor, valuationMode);
}

export async function fetchRouteWalletAPI(
  walletCards: string[],
  monthlySpend: Record<string, number>,
  valuationMode: string = "default"
): Promise<WalletStrategyResponse> {
  try {
    const res = await fetch(`${API_BASE_URL}/api/route-wallet`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ wallet_cards: walletCards, monthly_spend: monthlySpend, valuation_mode: valuationMode, include_ai: true })
    });
    if (res.ok) {
      return await res.json();
    }
  } catch {
    // Graceful fallback to client math
  }
  return findOptimalWalletStrategyClient(walletCards, monthlySpend, valuationMode);
}

export async function fetchCopilotAPI(message: string, history: Array<{ role: string; content: string }>): Promise<string> {
  try {
    const res = await fetch(`${API_BASE_URL}/api/copilot`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message, history })
    });
    if (res.ok) {
      const data = await res.json();
      return data.reply;
    }
  } catch {
    // Fallback response
  }
  return "SwipeSmart AI is analyzing your credit card query. Check capping limits and vendor reward rules in the Rules Hub!";
}
