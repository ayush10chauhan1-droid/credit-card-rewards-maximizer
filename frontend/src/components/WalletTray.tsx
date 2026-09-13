import React, { useState } from 'react';
import { Plus, Check, Wallet, X } from 'lucide-react';
import { CARDS_DATABASE, POPULAR_CARDS } from '../lib/data';
import { CreditCardSkin } from './CreditCardSkin';

interface WalletTrayProps {
  userWallet: string[];
  onToggleCard: (cardName: string) => void;
  scope: 'wallet' | 'all';
  onScopeChange: (scope: 'wallet' | 'all') => void;
}

export const WalletTray: React.FC<WalletTrayProps> = ({
  userWallet,
  onToggleCard,
  scope,
  onScopeChange
}) => {
  const [isAddModalOpen, setIsAddModalOpen] = useState(false);
  const [filterBank, setFilterBank] = useState('All');

  const banks = ['All', 'HDFC Bank', 'SBI Card', 'Axis Bank', 'ICICI Bank', 'American Express', 'Federal Bank'];

  const filteredCards = POPULAR_CARDS.filter((c) => {
    if (filterBank === 'All') return true;
    return CARDS_DATABASE[c]?.bank === filterBank;
  });

  return (
    <div className="space-y-4">
      {/* Wallet Controls & Scope Switcher */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
        <div className="flex items-center space-x-2">
          <Wallet className="w-5 h-5 text-indigo-400" />
          <h3 className="text-sm sm:text-base font-extrabold text-white tracking-tight">
            Your Digital Wallet ({userWallet.length} Cards Active)
          </h3>
        </div>

        <div className="flex items-center space-x-2">
          {/* Scope Radio / Toggle */}
          <div className="p-1 rounded-xl bg-obsidian-800 border border-white/10 flex text-xs font-semibold">
            <button
              type="button"
              onClick={() => onScopeChange('wallet')}
              className={`px-3 py-1 rounded-lg transition ${
                scope === 'wallet'
                  ? 'bg-indigo-600 text-white shadow-glow-indigo'
                  : 'text-slate-400 hover:text-white'
              }`}
            >
              My Wallet
            </button>
            <button
              type="button"
              onClick={() => onScopeChange('all')}
              className={`px-3 py-1 rounded-lg transition ${
                scope === 'all'
                  ? 'bg-indigo-600 text-white shadow-glow-indigo'
                  : 'text-slate-400 hover:text-white'
              }`}
            >
              All 26 Cards
            </button>
          </div>

          {/* Add Card Button */}
          <button
            type="button"
            onClick={() => setIsAddModalOpen(true)}
            className="px-3 py-1.5 rounded-xl bg-white/10 hover:bg-white/20 text-white font-bold text-xs flex items-center space-x-1.5 transition"
          >
            <Plus className="w-3.5 h-3.5" />
            <span className="hidden sm:inline">Manage Cards</span>
          </button>
        </div>
      </div>

      {/* Horizontal Interactive Card Carousel */}
      <div className="flex space-x-4 overflow-x-auto pb-4 pt-1 px-1 no-scrollbar">
        {userWallet.map((cardName) => (
          <div key={cardName} className="shrink-0">
            <CreditCardSkin
              cardName={cardName}
              size="md"
              isSelected={true}
              onToggleSelect={onToggleCard}
              showSpendCap={true}
              spendCapRemaining={4200}
              totalCap={5000}
            />
          </div>
        ))}

        {/* Quick Add Placeholder Card */}
        <button
          type="button"
          onClick={() => setIsAddModalOpen(true)}
          className="w-72 h-44 sm:w-80 sm:h-48 rounded-2xl border-2 border-dashed border-white/15 hover:border-indigo-400/50 bg-obsidian-800/40 hover:bg-obsidian-800 transition flex flex-col items-center justify-center space-y-2 text-slate-400 hover:text-white shrink-0 group"
        >
          <div className="w-10 h-10 rounded-full bg-white/5 border border-white/10 group-hover:border-indigo-500/50 flex items-center justify-center transition">
            <Plus className="w-5 h-5 text-indigo-400" />
          </div>
          <span className="text-xs font-bold">Add Another Card</span>
          <span className="text-[10px] text-slate-500">26 Premier Indian Cards</span>
        </button>
      </div>

      {/* Card Selection Modal */}
      {isAddModalOpen && (
        <div className="fixed inset-0 z-50 bg-black/80 backdrop-blur-md flex items-center justify-center p-4">
          <div className="w-full max-w-2xl max-h-[85vh] rounded-3xl bg-obsidian-900 border border-white/15 shadow-2xl flex flex-col overflow-hidden">
            {/* Modal Header */}
            <div className="p-5 border-b border-white/10 flex items-center justify-between bg-obsidian-850">
              <div>
                <h3 className="text-lg font-bold text-white">Select Cards for Your Wallet</h3>
                <p className="text-xs text-slate-400">Toggle cards you carry to customize reward calculations.</p>
              </div>
              <button
                type="button"
                onClick={() => setIsAddModalOpen(false)}
                className="p-1.5 rounded-lg text-slate-400 hover:text-white hover:bg-white/10"
              >
                <X className="w-5 h-5" />
              </button>
            </div>

            {/* Bank Filter Tabs */}
            <div className="p-3 border-b border-white/5 flex items-center space-x-1.5 overflow-x-auto no-scrollbar bg-obsidian-950/50 text-xs">
              {banks.map((b) => (
                <button
                  key={b}
                  type="button"
                  onClick={() => setFilterBank(b)}
                  className={`px-3 py-1 rounded-full shrink-0 transition font-medium ${
                    filterBank === b
                      ? 'bg-indigo-600 text-white'
                      : 'bg-white/5 text-slate-400 hover:text-white'
                  }`}
                >
                  {b}
                </button>
              ))}
            </div>

            {/* Cards List */}
            <div className="flex-1 p-4 overflow-y-auto space-y-2">
              {filteredCards.map((cardName) => {
                const card = CARDS_DATABASE[cardName];
                const isSelected = userWallet.includes(cardName);

                return (
                  <div
                    key={cardName}
                    onClick={() => onToggleCard(cardName)}
                    className={`p-3.5 rounded-2xl border transition cursor-pointer flex items-center justify-between ${
                      isSelected
                        ? 'bg-indigo-950/30 border-indigo-500/50 ring-1 ring-indigo-500/30'
                        : 'bg-obsidian-800 border-white/10 hover:border-white/20'
                    }`}
                  >
                    <div className="space-y-0.5">
                      <div className="flex items-center space-x-2">
                        <span className="font-bold text-white text-sm">{cardName}</span>
                        <span className="text-[10px] px-2 py-0.5 rounded-full bg-white/5 text-slate-400 font-mono">
                          {card.network}
                        </span>
                      </div>
                      <p className="text-xs text-slate-400 line-clamp-1">{card.summary}</p>
                      <div className="text-[11px] text-slate-500">
                        Fee: {card.annual_fee === 0 ? 'Free' : `₹${card.annual_fee.toLocaleString()}/yr`} • {card.tier}
                      </div>
                    </div>

                    <div className={`w-6 h-6 rounded-full flex items-center justify-center transition shrink-0 ml-3 ${
                      isSelected ? 'bg-emerald-500 text-black shadow-glow-emerald' : 'border border-white/30'
                    }`}>
                      {isSelected && <Check className="w-3.5 h-3.5 stroke-[3]" />}
                    </div>
                  </div>
                );
              })}
            </div>

            {/* Modal Footer */}
            <div className="p-4 border-t border-white/10 bg-obsidian-850 flex justify-end">
              <button
                type="button"
                onClick={() => setIsAddModalOpen(false)}
                className="px-5 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs shadow-glow-indigo transition"
              >
                Done ({userWallet.length} Cards Selected)
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
