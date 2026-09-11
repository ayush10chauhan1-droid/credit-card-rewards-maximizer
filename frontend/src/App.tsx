import React, { useState, useMemo, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import {
  CreditCard,
  Zap,
  Layers,
  Sparkles,
  GitCompare,
  BookOpen,
  Sliders,
  DollarSign,
  TrendingUp,
  ShieldCheck,
  Search,
  ExternalLink
} from 'lucide-react';

import {
  CATEGORIES,
  POPULAR_CARDS,
  CARDS_DATABASE,
  VENDORS_METADATA
} from './lib/data';

import {
  compareCardsClient,
  findOptimalWalletStrategyClient,
  analyzeSpendGapsClient,
  recommendNextCardsClient,
  fetchCompareAPI,
  fetchRouteWalletAPI,
  SinglePurchaseResponse,
  WalletStrategyResponse,
  SpendGap,
  CardRecommendation
} from './lib/engine';

import { WalletTray } from './components/WalletTray';
import { Omnibox } from './components/Omnibox';
import { WinningSwipeHero } from './components/WinningSwipeHero';
import { WalletRouter } from './components/WalletRouter';
import { RewardLeaksRadar } from './components/RewardLeaksRadar';
import { CardComparisonMatrix } from './components/CardComparisonMatrix';
import { RAGKnowledgeHub } from './components/RAGKnowledgeHub';
import { CopilotDrawer } from './components/CopilotDrawer';

export function App() {
  // Navigation State
  const [activeTab, setActiveTab] = useState<'instant' | 'router' | 'matchmaker' | 'matrix' | 'hub'>('instant');

  // Wallet State (Defaults to premier cards)
  const [userWallet, setUserWallet] = useState<string[]>([
    "SBI Cashback Card",
    "HDFC Millennia",
    "Axis Ace",
    "HDFC Infinia Metal"
  ]);
  const [evalScope, setEvalScope] = useState<'wallet' | 'all'>('wallet');

  // Valuation Mode State
  const [valMode, setValMode] = useState<string>('default');

  // Tab 1: Instant Swipe Inputs
  const [spendCategory, setSpendCategory] = useState<string>('Dining');
  const [merchant, setMerchant] = useState<string | null>('Swiggy');
  const [purchaseAmount, setPurchaseAmount] = useState<number>(2500);

  // Tab 2: Monthly Budget Profile State
  const [monthlySpend, setMonthlySpend] = useState<Record<string, number>>({
    "Online Shopping": 15000,
    "Dining": 8000,
    "Grocery": 10000,
    "Travel": 12000,
    "Utilities": 5000,
    "Movies/Entertainment": 2000,
    "Fuel": 4000,
    "International": 0,
    "UPI": 3000,
    "Other": 5000
  });

  // Tab 3: Matchmaker Filters
  const [lifestyleFilter, setLifestyleFilter] = useState('All');
  const [maxFeeFilter, setMaxFeeFilter] = useState('Any Fee');

  // -------------------------------------------------------------------
  // Core Calculation Engines (Instant Client Computation)
  // -------------------------------------------------------------------
  const activeCardsToEvaluate = useMemo(() => {
    return evalScope === 'wallet' ? userWallet : POPULAR_CARDS;
  }, [evalScope, userWallet]);

  // Instant Swipe Calculation
  const singleComparison: SinglePurchaseResponse = useMemo(() => {
    return compareCardsClient(activeCardsToEvaluate, spendCategory, purchaseAmount, merchant, valMode);
  }, [activeCardsToEvaluate, spendCategory, purchaseAmount, merchant, valMode]);

  // Multi-Card Wallet Strategy Calculation
  const walletStrategy: WalletStrategyResponse = useMemo(() => {
    return findOptimalWalletStrategyClient(userWallet, monthlySpend, valMode);
  }, [userWallet, monthlySpend, valMode]);

  // Spend Gaps Analysis
  const spendGaps: SpendGap[] = useMemo(() => {
    return analyzeSpendGapsClient(userWallet, monthlySpend);
  }, [userWallet, monthlySpend]);

  // Recommended Next Cards
  const matchmakerRecs: CardRecommendation[] = useMemo(() => {
    const feeLimit = maxFeeFilter === 'Zero Fee Only' ? 0
      : maxFeeFilter === 'Under ₹1,000' ? 1000
      : maxFeeFilter === 'Under ₹3,000' ? 3000
      : null;
    return recommendNextCardsClient(userWallet, monthlySpend, lifestyleFilter, feeLimit);
  }, [userWallet, monthlySpend, lifestyleFilter, maxFeeFilter]);

  // Toggle card in wallet
  const handleToggleCardInWallet = (cardName: string) => {
    if (userWallet.includes(cardName)) {
      if (userWallet.length > 1) {
        setUserWallet(userWallet.filter(c => c !== cardName));
      }
    } else {
      setUserWallet([...userWallet, cardName]);
    }
  };

  // Preset budget apply handler
  const handleApplyPreset = (presetName: string) => {
    if (presetName === 'Urban Tech Pro') {
      setMonthlySpend({
        "Online Shopping": 20000, "Dining": 12000, "Grocery": 12000, "Travel": 10000,
        "Utilities": 6000, "Movies/Entertainment": 3000, "Fuel": 3000, "International": 0, "UPI": 4000, "Other": 5000
      });
    } else if (presetName === 'High Flyer') {
      setMonthlySpend({
        "Online Shopping": 25000, "Dining": 20000, "Grocery": 15000, "Travel": 50000,
        "Utilities": 8000, "Movies/Entertainment": 5000, "Fuel": 7000, "International": 15000, "UPI": 5000, "Other": 10000
      });
    } else if (presetName === 'Family Household') {
      setMonthlySpend({
        "Online Shopping": 15000, "Dining": 8000, "Grocery": 25000, "Travel": 5000,
        "Utilities": 12000, "Movies/Entertainment": 4000, "Fuel": 6000, "International": 0, "UPI": 5000, "Other": 8000
      });
    } else if (presetName === 'Minimalist') {
      setMonthlySpend({
        "Online Shopping": 8000, "Dining": 5000, "Grocery": 8000, "Travel": 2000,
        "Utilities": 4000, "Movies/Entertainment": 1500, "Fuel": 2500, "International": 0, "UPI": 2000, "Other": 2000
      });
    }
  };

  return (
    <div className="min-h-screen bg-obsidian-950 text-slate-100 flex flex-col">
      {/* Navigation Topbar */}
      <header className="sticky top-0 z-40 bg-obsidian-900/85 backdrop-blur-xl border-b border-white/10 px-4 sm:px-8 py-3.5">
        <div className="max-w-7xl mx-auto flex flex-col md:flex-row md:items-center justify-between gap-3">
          {/* Logo & Platform Tag */}
          <div className="flex items-center space-x-3">
            <div className="w-10 h-10 rounded-2xl bg-gradient-to-tr from-indigo-600 via-indigo-500 to-emerald-400 p-0.5 shadow-glow-indigo flex items-center justify-center">
              <CreditCard className="w-5 h-5 text-white" />
            </div>
            <div>
              <div className="flex items-center space-x-2">
                <span className="font-display font-extrabold text-lg sm:text-xl tracking-tight text-white">
                  SWIPESMART
                </span>
                <span className="px-2 py-0.5 rounded-full text-[10px] font-black uppercase tracking-wider bg-emerald-500/20 text-emerald-400 border border-emerald-500/30">
                  AI Enterprise
                </span>
              </div>
              <p className="text-[11px] text-slate-400 font-medium">India's Premier Credit Card Reward Maximizer</p>
            </div>
          </div>

          {/* Navigation Tabs */}
          <nav className="flex items-center space-x-1 overflow-x-auto no-scrollbar bg-obsidian-800/80 p-1.5 rounded-2xl border border-white/10 text-xs font-semibold">
            <button
              type="button"
              onClick={() => setActiveTab('instant')}
              className={`px-3.5 py-2 rounded-xl transition flex items-center space-x-1.5 shrink-0 ${
                activeTab === 'instant'
                  ? 'bg-gradient-to-r from-indigo-600 to-indigo-500 text-white shadow-glow-indigo'
                  : 'text-slate-400 hover:text-white'
              }`}
            >
              <Zap className="w-3.5 h-3.5 text-emerald-400" />
              <span>Instant Swipe</span>
            </button>

            <button
              type="button"
              onClick={() => setActiveTab('router')}
              className={`px-3.5 py-2 rounded-xl transition flex items-center space-x-1.5 shrink-0 ${
                activeTab === 'router'
                  ? 'bg-gradient-to-r from-indigo-600 to-indigo-500 text-white shadow-glow-indigo'
                  : 'text-slate-400 hover:text-white'
              }`}
            >
              <Layers className="w-3.5 h-3.5" />
              <span>Multi-Card Router</span>
            </button>

            <button
              type="button"
              onClick={() => setActiveTab('matchmaker')}
              className={`px-3.5 py-2 rounded-xl transition flex items-center space-x-1.5 shrink-0 ${
                activeTab === 'matchmaker'
                  ? 'bg-gradient-to-r from-indigo-600 to-indigo-500 text-white shadow-glow-indigo'
                  : 'text-slate-400 hover:text-white'
              }`}
            >
              <Sparkles className="w-3.5 h-3.5 text-amber-400" />
              <span>Matchmaker</span>
            </button>

            <button
              type="button"
              onClick={() => setActiveTab('matrix')}
              className={`px-3.5 py-2 rounded-xl transition flex items-center space-x-1.5 shrink-0 ${
                activeTab === 'matrix'
                  ? 'bg-gradient-to-r from-indigo-600 to-indigo-500 text-white shadow-glow-indigo'
                  : 'text-slate-400 hover:text-white'
              }`}
            >
              <GitCompare className="w-3.5 h-3.5" />
              <span>Card Matrix</span>
            </button>

            <button
              type="button"
              onClick={() => setActiveTab('hub')}
              className={`px-3.5 py-2 rounded-xl transition flex items-center space-x-1.5 shrink-0 ${
                activeTab === 'hub'
                  ? 'bg-gradient-to-r from-indigo-600 to-indigo-500 text-white shadow-glow-indigo'
                  : 'text-slate-400 hover:text-white'
              }`}
            >
              <BookOpen className="w-3.5 h-3.5" />
              <span>Rules Hub</span>
            </button>
          </nav>

          {/* Point Redemption Valuation Mode */}
          <div className="hidden lg:flex items-center space-x-2 text-xs">
            <span className="text-slate-500 font-medium">Valuation:</span>
            <select
              value={valMode}
              onChange={(e) => setValMode(e.target.value)}
              className="bg-obsidian-800 border border-white/10 rounded-xl px-2.5 py-1.5 text-slate-200 focus:outline-none focus:border-indigo-500 text-xs"
            >
              <option value="default">Optimal Value (Best)</option>
              <option value="cash">Direct Statement Cash</option>
              <option value="flight_hotel">Flights & Hotels (SmartBuy)</option>
              <option value="air_miles">Airline Miles (Accor/AI)</option>
              <option value="vouchers">Brand Shopping Vouchers</option>
            </select>
          </div>
        </div>
      </header>

      {/* Main Content Body */}
      <main className="flex-1 max-w-7xl mx-auto w-full p-4 sm:p-8 space-y-8">
        {/* Interactive Digital Card Tray (Always accessible at top) */}
        <section className="p-6 rounded-3xl bg-obsidian-900 border border-white/10 shadow-2xl">
          <WalletTray
            userWallet={userWallet}
            onToggleCard={handleToggleCardInWallet}
            scope={evalScope}
            onScopeChange={setEvalScope}
          />
        </section>

        {/* Tab Content Views */}
        <AnimatePresence mode="wait">
          {activeTab === 'instant' && (
            <motion.section
              key="instant"
              initial={{ opacity: 0, y: 10 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -10 }}
              transition={{ duration: 0.2 }}
              className="space-y-6"
            >
              {/* Smart Merchant Omnibox */}
              <div className="p-6 sm:p-8 rounded-3xl bg-obsidian-900 border border-white/10 shadow-xl">
                <Omnibox
                  selectedCategory={spendCategory}
                  selectedVendor={merchant}
                  onSelectMerchant={(cat, ven) => {
                    setSpendCategory(cat);
                    setMerchant(ven);
                  }}
                  amount={purchaseAmount}
                  onAmountChange={setPurchaseAmount}
                />
              </div>

              {/* The "Winning Swipe" Spotlight Engine */}
              <WinningSwipeHero
                data={singleComparison}
                amount={purchaseAmount}
                category={spendCategory}
                vendor={merchant}
              />
            </motion.section>
          )}

          {activeTab === 'router' && (
            <motion.section
              key="router"
              initial={{ opacity: 0, y: 10 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -10 }}
              transition={{ duration: 0.2 }}
            >
              <WalletRouter
                strategy={walletStrategy}
                monthlySpend={monthlySpend}
                onUpdateCategorySpend={(cat, val) => {
                  setMonthlySpend({ ...monthlySpend, [cat]: val });
                }}
                onApplyPreset={handleApplyPreset}
                walletCards={userWallet}
              />
            </motion.section>
          )}

          {activeTab === 'matchmaker' && (
            <motion.section
              key="matchmaker"
              initial={{ opacity: 0, y: 10 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -10 }}
              transition={{ duration: 0.2 }}
            >
              <RewardLeaksRadar
                gaps={spendGaps}
                recommendations={matchmakerRecs}
                onAddCardToWallet={handleToggleCardInWallet}
                lifestyleFilter={lifestyleFilter}
                onLifestyleChange={setLifestyleFilter}
                maxFeeFilter={maxFeeFilter}
                onMaxFeeChange={setMaxFeeFilter}
              />
            </motion.section>
          )}

          {activeTab === 'matrix' && (
            <motion.section
              key="matrix"
              initial={{ opacity: 0, y: 10 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -10 }}
              transition={{ duration: 0.2 }}
            >
              <CardComparisonMatrix />
            </motion.section>
          )}

          {activeTab === 'hub' && (
            <motion.section
              key="hub"
              initial={{ opacity: 0, y: 10 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -10 }}
              transition={{ duration: 0.2 }}
            >
              <RAGKnowledgeHub />
            </motion.section>
          )}
        </AnimatePresence>
      </main>

      {/* Floating SwipeSmart Copilot Drawer */}
      <CopilotDrawer />

      {/* Footer */}
      <footer className="mt-12 py-8 border-t border-white/10 text-center text-xs text-slate-500 space-y-1">
        <p className="font-medium text-slate-400">
          SwipeSmart AI Enterprise v3.0 — India's Premier Credit Card Reward Optimization Engine
        </p>
        <p>
          26 Premier Indian Cards • Real Capping Rules Factored • Gemini 2.5 RAG Advisor
        </p>
      </footer>
    </div>
  );
}

export default App;
