import React from 'react';
import { motion } from 'framer-motion';
import { Sliders, ArrowRight, ShieldCheck, CheckCircle2, Layers } from 'lucide-react';
import { CATEGORIES, CATEGORY_ICONS } from '../lib/data';
import { WalletStrategyResponse } from '../lib/engine';

interface WalletRouterProps {
  strategy: WalletStrategyResponse;
  monthlySpend: Record<string, number>;
  onUpdateCategorySpend: (category: string, value: number) => void;
  onApplyPreset: (presetName: string) => void;
  walletCards?: string[];
}

export const WalletRouter: React.FC<WalletRouterProps> = ({
  strategy,
  monthlySpend,
  onUpdateCategorySpend,
  onApplyPreset,
  walletCards: _walletCards
}) => {
  const totalMonthlySpend = Object.values(monthlySpend).reduce((a, b) => a + b, 0);
  const totalAnnualSpend = totalMonthlySpend * 12;

  const presets = [
    { name: "Urban Tech Pro", amount: "₹70k/mo", desc: "Heavy online, dining & gadgets" },
    { name: "High Flyer", amount: "₹1.5L/mo", desc: "Flights, luxury hotels & premium dining" },
    { name: "Family Household", amount: "₹85k/mo", desc: "Groceries, utility bills & education" },
    { name: "Minimalist", amount: "₹35k/mo", desc: "Essential bills & light shopping" }
  ];

  return (
    <div className="space-y-8">
      {/* Top Header & Presets */}
      <div className="p-6 sm:p-8 rounded-3xl bg-obsidian-800 border border-white/10 space-y-6">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
          <div>
            <div className="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-indigo-500/10 border border-indigo-500/20 text-indigo-400 text-xs font-bold uppercase tracking-wider mb-2">
              <Layers className="w-3.5 h-3.5" />
              <span>Multi-Card Routing Engine</span>
            </div>
            <h2 className="text-2xl sm:text-3xl font-extrabold text-white tracking-tight">
              Monthly Budget Allocation Visualizer
            </h2>
            <p className="text-slate-400 text-sm mt-1 max-w-2xl">
              Configure your typical monthly expenditures. Our mathematical routing algorithm solves the multi-card portfolio problem to route every single rupee to its highest-yield card.
            </p>
          </div>

          {/* Aggregate Totals Pill */}
          <div className="p-4 rounded-2xl bg-obsidian-900 border border-white/10 shrink-0 text-right">
            <div className="text-xs text-slate-400 uppercase font-semibold">Total Monthly Budget</div>
            <div className="text-2xl font-black font-mono text-emerald-400">
              ₹{totalMonthlySpend.toLocaleString()}
            </div>
            <div className="text-[11px] text-slate-500 font-mono">
              ₹{totalAnnualSpend.toLocaleString()} / year
            </div>
          </div>
        </div>

        {/* Preset Selector Chips */}
        <div>
          <span className="text-xs font-bold text-slate-400 uppercase tracking-wider block mb-3">
            Quick Budget Presets
          </span>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3">
            {presets.map((p) => (
              <button
                key={p.name}
                type="button"
                onClick={() => onApplyPreset(p.name)}
                className="p-3.5 rounded-2xl bg-obsidian-750 border border-white/10 hover:border-indigo-500/40 hover:bg-obsidian-700 transition text-left group"
              >
                <div className="flex justify-between items-center mb-1">
                  <span className="font-bold text-sm text-white group-hover:text-indigo-300 transition">
                    {p.name}
                  </span>
                  <span className="text-xs font-mono font-bold text-emerald-400 bg-emerald-500/10 px-2 py-0.5 rounded-full">
                    {p.amount}
                  </span>
                </div>
                <p className="text-[11px] text-slate-400 line-clamp-1">{p.desc}</p>
              </button>
            ))}
          </div>
        </div>
      </div>

      {/* Spend Sliders Grid */}
      <div className="space-y-4">
        <h3 className="text-xs font-bold text-slate-400 uppercase tracking-wider flex items-center gap-2">
          <Sliders className="w-3.5 h-3.5 text-indigo-400" /> Adjust Monthly Spend By Category
        </h3>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-3">
          {CATEGORIES.map((cat) => {
            const val = monthlySpend[cat] || 0;
            const icon = CATEGORY_ICONS[cat] || '📌';
            const assignment = strategy.category_assignments?.[cat];

            return (
              <div
                key={cat}
                className="p-4 rounded-2xl bg-obsidian-800 border border-white/10 space-y-2.5 hover:border-white/20 transition"
              >
                <div className="flex items-center justify-between">
                  <span className="text-xs font-bold text-slate-300 flex items-center gap-1.5 truncate">
                    <span>{icon}</span> {cat}
                  </span>
                  <span className="text-sm font-extrabold font-mono text-emerald-400">
                    ₹{val.toLocaleString()}
                  </span>
                </div>

                {/* Slider Input */}
                <input
                  type="range"
                  min={0}
                  max={100000}
                  step={1000}
                  value={val}
                  onChange={(e) => onUpdateCategorySpend(cat, Number(e.target.value))}
                  className="w-full accent-emerald-500 cursor-pointer h-1.5 bg-obsidian-900 rounded-lg"
                />

                {/* Assigned Card Pill */}
                {assignment && val > 0 && (
                  <div className="pt-1.5 border-t border-white/5 flex items-center justify-between text-[11px]">
                    <span className="text-slate-400 truncate max-w-[110px]" title={assignment.assigned_card}>
                      💳 {assignment.assigned_card}
                    </span>
                    <span className="font-mono font-bold text-indigo-300 shrink-0">
                      +{assignment.effective_rate}%
                    </span>
                  </div>
                )}
              </div>
            );
          })}
        </div>
      </div>

      {/* High-Level Portfolio Strategy Dashboard */}
      {strategy.net_optimized_yearly_return > 0 && (
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          <div className="p-5 rounded-2xl bg-obsidian-800 border border-white/10">
            <span className="text-[11px] font-bold text-slate-400 uppercase tracking-wider block">
              Monthly Rewards Yield
            </span>
            <div className="text-2xl sm:text-3xl font-extrabold font-mono text-emerald-400 mt-1">
              ₹{strategy.total_optimized_monthly_reward.toFixed(2)}
            </div>
            <span className="text-[11px] text-slate-500">Auto-credited or points value</span>
          </div>

          <div className="p-5 rounded-2xl bg-emerald-500/10 border border-emerald-500/25">
            <span className="text-[11px] font-bold text-emerald-400 uppercase tracking-wider block">
              Net Annual Profit (After Fees)
            </span>
            <div className="text-2xl sm:text-3xl font-extrabold font-mono text-emerald-300 mt-1">
              ₹{strategy.net_optimized_yearly_return.toLocaleString()}
            </div>
            <span className="text-[11px] text-emerald-400/80">Accounted for non-waived card fees</span>
          </div>

          <div className="p-5 rounded-2xl bg-indigo-500/10 border border-indigo-500/25">
            <span className="text-[11px] font-bold text-indigo-400 uppercase tracking-wider block">
              Effective Wallet ROI
            </span>
            <div className="text-2xl sm:text-3xl font-extrabold font-mono text-indigo-300 mt-1">
              {strategy.optimized_roi_pct}%
            </div>
            <span className="text-[11px] text-indigo-400/80">Net return over total annual spend</span>
          </div>

          <div className="p-5 rounded-2xl bg-amber-500/10 border border-amber-500/25">
            <span className="text-[11px] font-bold text-amber-400 uppercase tracking-wider block">
              Multi-Card Synergy Bonus
            </span>
            <div className="text-2xl sm:text-3xl font-extrabold font-mono text-amber-300 mt-1">
              +₹{strategy.synergy_vs_single.toLocaleString()}/yr
            </div>
            <span className="text-[11px] text-amber-400/80">
              vs swiping only {strategy.best_single_card?.card}
            </span>
          </div>
        </div>
      )}

      {/* Interactive Category-to-Card Routing Flow Diagram */}
      <div className="space-y-4">
        <h3 className="text-xs font-bold text-slate-400 uppercase tracking-wider">
          Category-by-Category Rupee Routing
        </h3>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
          {Object.entries(strategy.category_assignments || {}).map(([cat, assign]) => {
            if (assign.spend <= 0) return null;
            return (
              <motion.div
                key={cat}
                initial={{ opacity: 0, y: 10 }}
                animate={{ opacity: 1, y: 0 }}
                className="p-4 rounded-2xl bg-obsidian-800 border border-white/10 flex items-center justify-between gap-4 hover:border-indigo-500/30 transition"
              >
                {/* Left: Spend Category */}
                <div className="space-y-0.5">
                  <div className="text-xs font-bold text-white flex items-center gap-1.5">
                    <span>{CATEGORY_ICONS[cat] || '📌'}</span> {cat}
                  </div>
                  <div className="text-xs font-mono text-slate-400">
                    ₹{assign.spend.toLocaleString()}/mo
                  </div>
                </div>

                {/* Center Routing Arrow */}
                <div className="flex flex-col items-center shrink-0">
                  <span className="text-[10px] font-mono text-emerald-400 font-bold mb-0.5">
                    {assign.effective_rate}%
                  </span>
                  <ArrowRight className="w-4 h-4 text-slate-500" />
                </div>

                {/* Right: Assigned Card & Yield */}
                <div className="text-right space-y-0.5">
                  <div className="text-xs font-bold text-indigo-300 truncate max-w-[160px]" title={assign.assigned_card}>
                    {assign.assigned_card}
                  </div>
                  <div className="text-xs font-mono font-extrabold text-emerald-400">
                    +₹{assign.monthly_reward.toFixed(2)}/mo
                  </div>
                </div>
              </motion.div>
            );
          })}
        </div>
      </div>

      {/* Annual Fee Waiver Progress Bar Tracker */}
      {strategy.card_fee_details && strategy.card_fee_details.length > 0 && (
        <div className="p-6 rounded-3xl bg-obsidian-800 border border-white/10 space-y-4">
          <h3 className="text-xs font-bold text-slate-400 uppercase tracking-wider flex items-center gap-2">
            <ShieldCheck className="w-4 h-4 text-emerald-400" /> Annual Spend-Based Fee Waiver Status
          </h3>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            {strategy.card_fee_details.map((cf) => {
              if (cf.base_fee === 0) {
                return (
                  <div key={cf.card} className="p-4 rounded-2xl bg-obsidian-850 border border-white/5 space-y-1">
                    <div className="flex justify-between items-center text-xs">
                      <span className="font-bold text-slate-200">{cf.card}</span>
                      <span className="text-emerald-400 font-bold text-[11px] bg-emerald-500/10 px-2 py-0.5 rounded-full">
                        Lifetime Free
                      </span>
                    </div>
                    <p className="text-[11px] text-slate-400">No annual fee or minimum spend required.</p>
                  </div>
                );
              }

              const progressPct = cf.waiver_spend_target > 0
                ? Math.min(100, Math.round((cf.routed_spend / cf.waiver_spend_target) * 100))
                : 0;

              return (
                <div key={cf.card} className="p-4 rounded-2xl bg-obsidian-850 border border-white/10 space-y-2.5">
                  <div className="flex justify-between items-center text-xs">
                    <span className="font-bold text-slate-200 truncate max-w-[150px]" title={cf.card}>
                      {cf.card}
                    </span>
                    {cf.waived ? (
                      <span className="text-emerald-400 font-bold text-[10px] bg-emerald-500/10 px-2 py-0.5 rounded-full flex items-center gap-1">
                        <CheckCircle2 className="w-3 h-3" /> Fee Waived
                      </span>
                    ) : (
                      <span className="text-amber-400 font-bold text-[10px] bg-amber-500/10 px-2 py-0.5 rounded-full">
                        Fee: ₹{cf.base_fee.toLocaleString()}
                      </span>
                    )}
                  </div>

                  {cf.waiver_spend_target > 0 ? (
                    <div>
                      <div className="flex justify-between text-[10px] text-slate-400 font-mono mb-1">
                        <span>Routed: ₹{cf.routed_spend.toLocaleString()}</span>
                        <span>Target: ₹{cf.waiver_spend_target.toLocaleString()}</span>
                      </div>
                      <div className="w-full h-1.5 rounded-full bg-white/10 overflow-hidden">
                        <div
                          className={`h-full rounded-full transition-all duration-500 ${
                            cf.waived ? 'bg-emerald-400' : 'bg-amber-400'
                          }`}
                          style={{ width: `${progressPct}%` }}
                        />
                      </div>
                    </div>
                  ) : (
                    <p className="text-[11px] text-slate-400">No official spend fee waiver criteria.</p>
                  )}
                </div>
              );
            })}
          </div>
        </div>
      )}
    </div>
  );
};
