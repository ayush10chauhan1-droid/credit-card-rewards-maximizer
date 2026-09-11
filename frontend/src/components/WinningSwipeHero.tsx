import React from 'react';
import { motion } from 'framer-motion';
import { Crown, Sparkles, TrendingUp, AlertTriangle, ArrowRight, ShieldAlert, Award } from 'lucide-react';
import confetti from 'canvas-confetti';
import { CreditCardSkin } from './CreditCardSkin';
import { SinglePurchaseResponse } from '../lib/engine';
import { CARDS_DATABASE } from '../lib/data';

interface WinningSwipeHeroProps {
  data: SinglePurchaseResponse;
  amount: number;
  category: string;
  vendor?: string | null;
}

export const WinningSwipeHero: React.FC<WinningSwipeHeroProps> = ({
  data,
  amount,
  category,
  vendor
}) => {
  const { results, best_card, best_reward, runner_up, runner_up_card, savings_delta, tips, ai_rationale } = data;

  if (!best_card || results.length === 0) {
    return (
      <div className="p-8 rounded-3xl bg-obsidian-800 border border-white/10 text-center">
        <p className="text-slate-400">Select cards in your wallet to generate recommendations.</p>
      </div>
    );
  }

  const bestCardInfo = CARDS_DATABASE[best_card];
  const bestResult = results[0];
  const roiPct = amount > 0 ? ((best_reward / amount) * 100).toFixed(2) : "0.00";

  // Trigger subtle confetti on render if reward is high (> ₹250)
  React.useEffect(() => {
    if (best_reward >= 250) {
      confetti({
        particleCount: 35,
        spread: 60,
        origin: { y: 0.7 },
        colors: ['#10B981', '#6366F1', '#F59E0B']
      });
    }
  }, [best_card, amount, vendor]);

  // Breakdown calculation:
  // Base points rate (usually 1% to 3.3%) vs accelerated partner boost
  const baseRate = bestCardInfo?.rewards?.['Other'] || 1.0;
  const baseReward = Math.round(amount * (baseRate / 100.0) * 100) / 100;
  const acceleratedReward = Math.max(0, Math.round((best_reward - baseReward) * 100) / 100);

  // Spend cap warning check
  const capNote = bestResult.cap_note;

  return (
    <div className="space-y-6">
      {/* Top Winning Spotlight Banner */}
      <motion.div
        initial={{ opacity: 0, y: 15 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.4 }}
        className="relative overflow-hidden rounded-3xl bg-gradient-to-b from-obsidian-800 to-obsidian-850 border border-white/15 p-6 sm:p-8 shadow-2xl"
      >
        {/* Ambient background glow */}
        <div className="absolute top-0 right-1/4 w-96 h-96 bg-emerald-500/10 rounded-full blur-3xl pointer-events-none" />
        <div className="absolute bottom-0 left-1/3 w-96 h-96 bg-indigo-500/10 rounded-full blur-3xl pointer-events-none" />

        <div className="relative z-10 grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
          {/* Left: Card Visual Presentation (5 Cols) */}
          <div className="lg:col-span-5 flex flex-col items-center justify-center">
            <div className="relative">
              <div className="absolute -top-3 left-1/2 -translate-x-1/2 z-20 flex items-center space-x-1.5 px-3 py-1 rounded-full bg-emerald-500 text-black font-extrabold text-xs tracking-wider uppercase shadow-glow-emerald">
                <Crown className="w-3.5 h-3.5 stroke-[2.5]" />
                <span>The Winning Swipe</span>
              </div>
              <CreditCardSkin
                cardName={best_card}
                highlightWinning={true}
                size="lg"
              />
            </div>
          </div>

          {/* Right: Net Reward, ROI, Breakdown & Missed Opportunity (7 Cols) */}
          <div className="lg:col-span-7 space-y-6">
            {/* Header / Transaction Summary */}
            <div>
              <div className="flex flex-wrap items-center gap-2 mb-1 text-xs text-slate-400">
                <span className="px-2.5 py-0.5 rounded-full bg-white/5 font-semibold text-slate-300">
                  {vendor ? `🏪 Merchant: ${vendor}` : `📂 Category: ${category}`}
                </span>
                <span>•</span>
                <span>Spend ₹{amount.toLocaleString()}</span>
              </div>
              <h2 className="text-2xl sm:text-3xl font-extrabold tracking-tight text-white flex items-center gap-2">
                Swipe {best_card}
              </h2>
            </div>

            {/* Primary Metrics Row */}
            <div className="grid grid-cols-2 sm:grid-cols-3 gap-3">
              {/* Metric 1: Net Reward Value */}
              <div className="p-4 rounded-2xl bg-emerald-500/10 border border-emerald-500/25">
                <span className="text-[11px] font-bold text-emerald-400 uppercase tracking-wider block">
                  Net Reward Earned
                </span>
                <span className="text-2xl sm:text-3xl font-extrabold font-mono text-emerald-300">
                  ₹{best_reward.toFixed(2)}
                </span>
              </div>

              {/* Metric 2: Effective ROI Rate */}
              <div className="p-4 rounded-2xl bg-indigo-500/10 border border-indigo-500/25">
                <span className="text-[11px] font-bold text-indigo-400 uppercase tracking-wider block">
                  Effective ROI Rate
                </span>
                <span className="text-2xl sm:text-3xl font-extrabold font-mono text-indigo-300">
                  {roiPct}%
                </span>
              </div>

              {/* Metric 3: Reward Multiplier Type */}
              <div className="p-4 rounded-2xl bg-white/5 border border-white/10 col-span-2 sm:col-span-1">
                <span className="text-[11px] font-bold text-slate-400 uppercase tracking-wider block">
                  Program Type
                </span>
                <span className="text-lg font-bold text-white capitalize flex items-center gap-1.5 mt-1">
                  <Award className="w-4 h-4 text-amber-400" />
                  {bestResult.type}
                </span>
              </div>
            </div>

            {/* Reward Points Breakdown Bar */}
            <div className="p-4 rounded-2xl bg-obsidian-900/80 border border-white/10 space-y-2">
              <div className="flex justify-between text-xs font-semibold">
                <span className="text-slate-400">Reward Value Composition</span>
                <span className="text-slate-200 font-mono">₹{best_reward.toFixed(2)} Total</span>
              </div>
              <div className="w-full h-2 rounded-full bg-white/10 overflow-hidden flex">
                <div
                  className="h-full bg-slate-400"
                  style={{ width: `${Math.min(100, (baseReward / Math.max(1, best_reward)) * 100)}%` }}
                  title={`Base Rewards: ₹${baseReward}`}
                />
                <div
                  className="h-full bg-emerald-400"
                  style={{ width: `${Math.min(100, (acceleratedReward / Math.max(1, best_reward)) * 100)}%` }}
                  title={`Accelerated Partner Boost: ₹${acceleratedReward}`}
                />
              </div>
              <div className="flex justify-between text-[11px] text-slate-400">
                <span className="flex items-center gap-1">
                  <span className="w-2 h-2 rounded-full bg-slate-400" /> Base ({baseRate}%): ₹{baseReward.toFixed(2)}
                </span>
                <span className="flex items-center gap-1 text-emerald-300">
                  <span className="w-2 h-2 rounded-full bg-emerald-400" /> Accelerated Partner Boost: +₹{acceleratedReward.toFixed(2)}
                </span>
              </div>
            </div>

            {/* Spend Cap Warning (if applicable) */}
            {capNote && (
              <div className="p-3.5 rounded-xl bg-amber-500/10 border border-amber-500/30 flex items-start space-x-3 text-amber-300 text-xs">
                <AlertTriangle className="w-4 h-4 shrink-0 mt-0.5 text-amber-400" />
                <div>
                  <span className="font-bold">Spend Cap Alert: </span>
                  <span>{capNote}</span>
                </div>
              </div>
            )}

            {/* "Next Best Alternative" (Opportunity Cost Card) */}
            {runner_up_card && savings_delta > 0 && (
              <div className="p-4 rounded-2xl bg-obsidian-900 border border-indigo-500/20 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3">
                <div className="flex items-center space-x-3">
                  <div className="w-8 h-8 rounded-full bg-indigo-500/20 border border-indigo-500/40 flex items-center justify-center text-indigo-300 font-bold text-xs">
                    #2
                  </div>
                  <div>
                    <div className="text-xs font-bold text-slate-200">
                      Alternative: {runner_up_card.card}
                    </div>
                    <div className="text-[11px] text-slate-400 font-mono">
                      Yields ₹{runner_up_card.reward.toFixed(2)} ({runner_up_card.rate}%)
                    </div>
                  </div>
                </div>

                <div className="sm:text-right">
                  <span className="text-[10px] uppercase font-bold text-rose-400 block tracking-wider">
                    Missed Opportunity
                  </span>
                  <span className="text-sm font-extrabold text-rose-300 font-mono">
                    -₹{savings_delta.toFixed(2)} less reward
                  </span>
                </div>
              </div>
            )}
          </div>
        </div>

        {/* AI Rationale Box */}
        {ai_rationale && (
          <div className="mt-6 pt-6 border-t border-white/10 flex items-start space-x-3 bg-indigo-950/20 p-4 rounded-2xl border border-indigo-500/20">
            <Sparkles className="w-5 h-5 text-indigo-400 shrink-0 mt-0.5" />
            <div>
              <div className="text-xs font-bold text-indigo-300 uppercase tracking-wider mb-1">
                SwipeSmart Neural Rationale
              </div>
              <p className="text-xs sm:text-sm text-slate-300 leading-relaxed">
                {ai_rationale}
              </p>
            </div>
          </div>
        )}
      </motion.div>

      {/* Runner-up Cards Grid */}
      {results.length > 1 && (
        <div className="space-y-3">
          <h3 className="text-xs font-bold text-slate-400 uppercase tracking-wider">
            All Evaluated Cards ({results.length})
          </h3>
          <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-3">
            {results.map((r, idx) => {
              const isWinner = idx === 0;
              return (
                <div
                  key={r.card}
                  className={`p-4 rounded-2xl transition border ${
                    isWinner
                      ? 'bg-emerald-950/30 border-emerald-500/40 ring-1 ring-emerald-500/30'
                      : 'bg-obsidian-800 border-white/10 hover:border-white/20'
                  }`}
                >
                  <div className="flex items-center justify-between text-xs mb-2">
                    <span className="font-bold text-slate-200 line-clamp-1">{r.card}</span>
                    <span className={`px-2 py-0.5 rounded text-[10px] font-mono font-bold ${
                      isWinner ? 'bg-emerald-500/20 text-emerald-300' : 'bg-white/5 text-slate-400'
                    }`}>
                      #{idx + 1}
                    </span>
                  </div>

                  <div className="flex items-baseline justify-between mb-1">
                    <span className="text-xl font-extrabold font-mono text-white">
                      ₹{r.reward.toFixed(2)}
                    </span>
                    <span className="text-xs font-bold font-mono text-indigo-300">
                      {r.rate}%
                    </span>
                  </div>

                  <p className="text-[11px] text-slate-400 truncate mb-2">{r.source}</p>

                  <div className="pt-2 border-t border-white/5 flex justify-between text-[10px] text-slate-500">
                    <span>Fee: ₹{r.annual_fee.toLocaleString()}</span>
                    <span>{r.network}</span>
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      )}
    </div>
  );
};
