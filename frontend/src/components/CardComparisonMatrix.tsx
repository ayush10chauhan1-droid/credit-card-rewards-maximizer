import React, { useState } from 'react';
import { CARDS_DATABASE, POPULAR_CARDS } from '../lib/data';
import { CreditCardSkin } from './CreditCardSkin';

export const CardComparisonMatrix: React.FC = () => {
  const [selectedCards, setSelectedCards] = useState<string[]>([
    "HDFC Infinia Metal",
    "SBI Cashback Card",
    "Axis Atlas",
    "ICICI Amazon Pay"
  ]);

  const handleToggleCard = (cardName: string) => {
    if (selectedCards.includes(cardName)) {
      if (selectedCards.length > 1) {
        setSelectedCards(selectedCards.filter(c => c !== cardName));
      }
    } else {
      if (selectedCards.length < 4) {
        setSelectedCards([...selectedCards, cardName]);
      } else {
        setSelectedCards([...selectedCards.slice(1), cardName]);
      }
    }
  };

  const categoriesToCompare = ["Online Shopping", "Dining", "Grocery", "Travel", "Utilities"];

  return (
    <div className="space-y-6">
      {/* Top Header & Selector */}
      <div className="p-6 sm:p-8 rounded-3xl bg-obsidian-800 border border-white/10 space-y-4">
        <div>
          <h2 className="text-xl sm:text-2xl font-extrabold text-white tracking-tight">
            Head-to-Head Card Comparison Matrix
          </h2>
          <p className="text-xs text-slate-400 mt-0.5">
            Select up to 4 credit cards to compare reward rates, forex markup, airport lounge rules, and fee waiver targets side-by-side.
          </p>
        </div>

        {/* Card Selector Chips */}
        <div className="flex flex-wrap gap-2 pt-2">
          {POPULAR_CARDS.slice(0, 12).map((c) => {
            const isSelected = selectedCards.includes(c);
            return (
              <button
                key={c}
                type="button"
                onClick={() => handleToggleCard(c)}
                className={`px-3 py-1.5 rounded-full text-xs font-semibold transition flex items-center space-x-1.5 ${
                  isSelected
                    ? 'bg-indigo-600 text-white shadow-glow-indigo border border-indigo-400/50'
                    : 'bg-obsidian-750 border border-white/10 text-slate-400 hover:text-white hover:border-white/20'
                }`}
              >
                <span>{isSelected ? '✓' : '+'}</span>
                <span>{c}</span>
              </button>
            );
          })}
        </div>
      </div>

      {/* Comparison Grid */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        {selectedCards.map((cardName) => {
          const card = CARDS_DATABASE[cardName];
          if (!card) return null;

          return (
            <div
              key={cardName}
              className="p-5 rounded-3xl bg-obsidian-800 border border-white/10 space-y-5 flex flex-col justify-between"
            >
              {/* Card Skin Miniature */}
              <div className="flex justify-center pt-2">
                <CreditCardSkin cardName={cardName} size="sm" isSelected={false} />
              </div>

              {/* Specs Table */}
              <div className="space-y-3 text-xs">
                {/* Annual Fee */}
                <div className="p-3 rounded-xl bg-obsidian-850 border border-white/5 flex justify-between items-center">
                  <span className="text-slate-400">Annual Fee</span>
                  <span className="font-mono font-extrabold text-white">
                    {card.annual_fee === 0 ? '₹0 (Free)' : `₹${card.annual_fee.toLocaleString()}`}
                  </span>
                </div>

                {/* Spend Fee Waiver */}
                <div className="flex justify-between items-center px-1">
                  <span className="text-slate-400">Spend Waiver:</span>
                  <span className="font-mono text-amber-300 font-semibold">
                    {card.fee_waiver_spend > 0 ? `₹${card.fee_waiver_spend.toLocaleString()}/yr` : 'None'}
                  </span>
                </div>

                {/* Forex Markup */}
                <div className="flex justify-between items-center px-1">
                  <span className="text-slate-400">Forex Markup:</span>
                  <span className={`font-mono font-bold ${card.forex_markup === 0 ? 'text-emerald-400' : 'text-slate-200'}`}>
                    {card.forex_markup}% {card.forex_markup === 0 && '⚡ Zero Forex'}
                  </span>
                </div>

                {/* Domestic Lounge */}
                <div className="flex justify-between items-start px-1 gap-2">
                  <span className="text-slate-400 shrink-0">Lounge:</span>
                  <span className="text-slate-200 text-right font-medium text-[11px] line-clamp-2">
                    {card.domestic_lounges}
                  </span>
                </div>

                {/* Reward Rates */}
                <div className="pt-2 border-t border-white/10 space-y-1.5">
                  <span className="text-[10px] font-bold text-slate-500 uppercase tracking-wider block mb-1">
                    Category Reward Rates
                  </span>
                  {categoriesToCompare.map((cat) => {
                    const rate = card.rewards?.[cat] || card.rewards?.['Other'] || 1.0;
                    return (
                      <div key={cat} className="flex justify-between items-center text-[11px]">
                        <span className="text-slate-400">{cat}</span>
                        <span className="font-mono font-bold text-emerald-400">{rate}%</span>
                      </div>
                    );
                  })}
                </div>
              </div>

              {/* Apply Button */}
              <div className="pt-3 border-t border-white/10">
                <a
                  href={card.apply_url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="w-full py-2 rounded-xl bg-white/10 hover:bg-white/20 text-white text-xs font-bold transition block text-center"
                >
                  Official Issuer Page ↗
                </a>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};
