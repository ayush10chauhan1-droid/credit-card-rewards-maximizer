import React from 'react';
import { motion } from 'framer-motion';
import { AlertOctagon, Sparkles, Plus, ExternalLink, ShieldCheck } from 'lucide-react';
import { SpendGap, CardRecommendation } from '../lib/engine';

interface RewardLeaksRadarProps {
  gaps: SpendGap[];
  recommendations: CardRecommendation[];
  onAddCardToWallet: (cardName: string) => void;
  lifestyleFilter: string;
  onLifestyleChange: (filter: string) => void;
  maxFeeFilter: string;
  onMaxFeeChange: (fee: string) => void;
}

export const RewardLeaksRadar: React.FC<RewardLeaksRadarProps> = ({
  gaps,
  recommendations,
  onAddCardToWallet,
  lifestyleFilter,
  onLifestyleChange,
  maxFeeFilter,
  onMaxFeeChange
}) => {
  const handleSimulate = (cardName: string) => {
    onAddCardToWallet(cardName);
  };

  return (
    <div className="space-y-8">
      {/* Detected Reward Leaks Radar */}
      <div className="p-6 sm:p-8 rounded-3xl bg-obsidian-800 border border-white/10 space-y-6">
        <div className="flex items-center space-x-2.5">
          <div className="w-8 h-8 rounded-full bg-rose-500/10 border border-rose-500/30 flex items-center justify-center text-rose-400">
            <AlertOctagon className="w-4 h-4" />
          </div>
          <div>
            <h2 className="text-xl sm:text-2xl font-extrabold text-white tracking-tight">
              Detected Reward Leaks & Spend Gaps
            </h2>
            <p className="text-xs text-slate-400">
              High-spend categories in your current wallet yielding low return (&lt; 2.5%).
            </p>
          </div>
        </div>

        {gaps.length === 0 ? (
          <div className="p-4 rounded-2xl bg-emerald-500/10 border border-emerald-500/20 text-emerald-300 text-xs flex items-center gap-2">
            <ShieldCheck className="w-4 h-4 text-emerald-400 shrink-0" />
            <span>Optimal wallet coverage! No significant reward leaks detected (&gt; ₹3,000/mo at &lt; 2.5%).</span>
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            {gaps.map((g) => (
              <motion.div
                key={g.category}
                initial={{ opacity: 0, scale: 0.95 }}
                animate={{ opacity: 1, scale: 1 }}
                className="p-5 rounded-2xl bg-gradient-to-b from-rose-950/20 to-obsidian-850 border border-rose-500/25 space-y-3"
              >
                <div className="flex justify-between items-center">
                  <span className="text-sm font-bold text-rose-200">{g.category}</span>
                  <span className="px-2 py-0.5 rounded-full text-[10px] font-bold uppercase tracking-wider bg-rose-500/20 text-rose-300 border border-rose-500/30">
                    {g.urgency} Leak
                  </span>
                </div>

                <div>
                  <div className="text-2xl font-black font-mono text-rose-400">
                    ~₹{g.annual_leak_estimate.toLocaleString()}/yr
                  </div>
                  <span className="text-[11px] text-slate-400">Annual reward money left on table</span>
                </div>

                <div className="text-xs text-slate-300 space-y-1 pt-2 border-t border-white/5">
                  <div className="flex justify-between">
                    <span className="text-slate-400">Monthly Spend:</span>
                    <span className="font-mono text-white">₹{g.monthly_spend.toLocaleString()}</span>
                  </div>
                  <div className="flex justify-between">
                    <span className="text-slate-400">Current Yield:</span>
                    <span className="font-mono text-rose-300 font-bold">{g.current_rate}% ({g.current_card})</span>
                  </div>
                  <div className="flex justify-between">
                    <span className="text-slate-400">Target Benchmark:</span>
                    <span className="font-mono text-emerald-400 font-bold">5.0%</span>
                  </div>
                </div>
              </motion.div>
            ))}
          </div>
        )}
      </div>

      {/* Top Card Recommendations & Matchmaker */}
      <div className="space-y-6">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
          <div>
            <h3 className="text-xl font-extrabold text-white tracking-tight flex items-center gap-2">
              <Sparkles className="w-5 h-5 text-indigo-400" /> Card Matchmaker — Top Portfolio Additions
            </h3>
            <p className="text-xs text-slate-400 mt-0.5">
              Ranked strictly by Net Incremental Annual Profit after deducting card fees.
            </p>
          </div>

          {/* Filters */}
          <div className="flex flex-wrap items-center gap-2 text-xs">
            <select
              value={lifestyleFilter}
              onChange={(e) => onLifestyleChange(e.target.value)}
              className="bg-obsidian-800 border border-white/15 rounded-xl px-3 py-2 text-slate-200 focus:outline-none focus:border-indigo-500"
            >
              <option value="All">All Card Lifestyles</option>
              <option value="Lifetime Free">Lifetime Free (LTF)</option>
              <option value="Pure Cashback">Pure Direct Cashback</option>
              <option value="Travel & Lounges">Travel & Lounges</option>
              <option value="Super Premium">Super Premium Metal</option>
            </select>

            <select
              value={maxFeeFilter}
              onChange={(e) => onMaxFeeChange(e.target.value)}
              className="bg-obsidian-800 border border-white/15 rounded-xl px-3 py-2 text-slate-200 focus:outline-none focus:border-indigo-500"
            >
              <option value="Any Fee">Any Annual Fee</option>
              <option value="Zero Fee Only">Zero Fee Only</option>
              <option value="Under ₹1,000">Fee Under ₹1,000</option>
              <option value="Under ₹3,000">Fee Under ₹3,000</option>
            </select>
          </div>
        </div>

        {/* Candidate Cards Grid */}
        {recommendations.length === 0 ? (
          <div className="p-8 rounded-3xl bg-obsidian-800 border border-white/10 text-center text-slate-400 text-sm">
            No unowned cards match your active filter criteria. Try resetting lifestyle or fee filters.
          </div>
        ) : (
          <div className="space-y-4">
            {recommendations.slice(0, 5).map((rec, idx) => {
              const isTop = idx === 0;
              return (
                <motion.div
                  key={rec.card}
                  initial={{ opacity: 0, y: 15 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: idx * 0.05 }}
                  className={`p-6 rounded-3xl transition duration-300 border ${
                    isTop
                      ? 'bg-gradient-to-r from-obsidian-800 via-obsidian-800 to-indigo-950/30 border-indigo-500/40 shadow-glow-indigo'
                      : 'bg-obsidian-800 border-white/10 hover:border-white/20'
                  }`}
                >
                  <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
                    {/* Left: Card Info */}
                    <div className="space-y-1.5">
                      <div className="flex items-center space-x-2">
                        <span className={`px-2.5 py-0.5 rounded-full text-[10px] font-extrabold uppercase tracking-wider ${
                          isTop ? 'bg-indigo-500 text-white shadow-glow-indigo' : 'bg-white/10 text-slate-300'
                        }`}>
                          {isTop ? '🥇 Top Match' : `#${idx + 1} Candidate`}
                        </span>
                        <span className="text-xs text-slate-400">
                          {rec.bank} • {rec.tier}
                        </span>
                      </div>

                      <h4 className="text-xl font-extrabold text-white tracking-tight">
                        {rec.card}
                      </h4>
                      <p className="text-xs text-slate-400 max-w-xl line-clamp-1">
                        {rec.summary}
                      </p>
                    </div>

                    {/* Right: Net Incremental Profit Metric */}
                    <div className="text-left md:text-right shrink-0">
                      <span className="text-[10px] font-bold text-slate-400 uppercase tracking-wider block">
                        Net Incremental Profit
                      </span>
                      <div className="text-2xl sm:text-3xl font-extrabold font-mono text-emerald-400">
                        +₹{rec.incremental_annual_profit.toLocaleString()}/yr
                      </div>
                      <span className="text-[11px] text-slate-500">
                        {rec.annual_fee === 0 ? 'Zero fee (100% pure upside)' : `After ₹${rec.annual_fee.toLocaleString()} annual fee`}
                      </span>
                    </div>
                  </div>

                  {/* Bottom Action & Conquered Categories */}
                  <div className="mt-4 pt-4 border-t border-white/10 flex flex-col sm:flex-row sm:items-center justify-between gap-3 text-xs">
                    <div className="text-slate-300 flex items-center gap-1.5 flex-wrap">
                      <span className="text-slate-400 font-semibold">Takes over:</span>
                      {rec.conquered_categories.length > 0 ? (
                        rec.conquered_categories.map((c) => (
                          <span key={c.category} className="px-2 py-0.5 rounded-md bg-white/5 border border-white/10 text-slate-200">
                            {c.category} ({c.new_rate}%)
                          </span>
                        ))
                      ) : (
                        <span className="text-slate-400">General portfolio rewards</span>
                      )}
                      <span className="text-slate-500">• Lounge: {rec.domestic_lounges}</span>
                    </div>

                    <div className="flex items-center space-x-2 shrink-0">
                      <button
                        type="button"
                        onClick={() => handleSimulate(rec.card)}
                        className="px-3.5 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs flex items-center gap-1.5 transition shadow-glow-indigo"
                      >
                        <Plus className="w-3.5 h-3.5" />
                        <span>Add to My Wallet & Recalculate</span>
                      </button>

                      <a
                        href={rec.apply_url}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="px-3 py-2 rounded-xl bg-white/5 hover:bg-white/10 text-slate-300 hover:text-white transition flex items-center gap-1"
                      >
                        <span>Apply</span>
                        <ExternalLink className="w-3 h-3" />
                      </a>
                    </div>
                  </div>
                </motion.div>
              );
            })}
          </div>
        )}
      </div>
    </div>
  );
};
