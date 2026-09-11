import React, { useState, useEffect, useRef } from 'react';
import { Search, Sparkles, X, ArrowRight, Tag } from 'lucide-react';
import { VENDORS_METADATA, CATEGORIES, CATEGORY_ICONS } from '../lib/data';

interface OmniboxProps {
  selectedCategory: string;
  selectedVendor: string | null;
  onSelectMerchant: (category: string, vendor: string | null) => void;
  amount: number;
  onAmountChange: (amount: number) => void;
}

export const Omnibox: React.FC<OmniboxProps> = ({
  selectedCategory,
  selectedVendor,
  onSelectMerchant,
  amount,
  onAmountChange
}) => {
  const [query, setQuery] = useState('');
  const [isOpen, setIsOpen] = useState(false);
  const containerRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLInputElement>(null);

  // Keyboard shortcut Cmd/Ctrl + K to focus search
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
        e.preventDefault();
        inputRef.current?.focus();
        setIsOpen(true);
      }
      if (e.key === 'Escape') {
        setIsOpen(false);
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, []);

  // Close dropdown on outside click
  useEffect(() => {
    const handleClickOutside = (e: MouseEvent) => {
      if (containerRef.current && !containerRef.current.contains(e.target as Node)) {
        setIsOpen(false);
      }
    };
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  // Filter merchants and categories based on search query
  const merchantEntries = Object.entries(VENDORS_METADATA);
  const filteredMerchants = merchantEntries.filter(([name, data]) => {
    const q = query.toLowerCase().trim();
    if (!q) return true;
    return name.toLowerCase().includes(q) || data.category.toLowerCase().includes(q) || data.description.toLowerCase().includes(q);
  });

  const filteredCategories = CATEGORIES.filter(cat => {
    const q = query.toLowerCase().trim();
    if (!q) return false;
    return cat.toLowerCase().includes(q);
  });

  const popularQuickPicks = [
    { label: "Swiggy", vendor: "Swiggy", category: "Dining", icon: "🍔" },
    { label: "Amazon", vendor: "Amazon", category: "Online Shopping", icon: "📦" },
    { label: "Blinkit", vendor: "Blinkit", category: "Grocery", icon: "⚡" },
    { label: "Zomato", vendor: "Zomato", category: "Dining", icon: "🍕" },
    { label: "MakeMyTrip", vendor: "MakeMyTrip", category: "Travel", icon: "✈️" },
    { label: "G-Pay Utilities", vendor: "Google Pay Utilities", category: "Utilities", icon: "💡" },
    { label: "BPCL Fuel", vendor: "BPCL Fuel", category: "Fuel", icon: "⛽" },
  ];

  const handlePickMerchant = (vendorName: string, category: string) => {
    onSelectMerchant(category, vendorName);
    setQuery(vendorName);
    setIsOpen(false);
  };

  const handlePickCategory = (category: string) => {
    onSelectMerchant(category, null);
    setQuery(category);
    setIsOpen(false);
  };

  const handleClear = () => {
    setQuery('');
    onSelectMerchant('Online Shopping', null);
    inputRef.current?.focus();
  };

  return (
    <div ref={containerRef} className="relative w-full space-y-3">
      {/* Top Search & Amount Grid */}
      <div className="grid grid-cols-1 md:grid-cols-12 gap-3 items-center">
        {/* Omnibox Input (8 Cols) */}
        <div className="md:col-span-8 relative">
          <div
            className={`relative flex items-center bg-obsidian-800 border rounded-2xl px-4 py-3.5 transition-all duration-300 ${
              isOpen
                ? 'border-indigo-500 shadow-glow-indigo bg-obsidian-750 ring-2 ring-indigo-500/20'
                : 'border-white/10 hover:border-white/20'
            }`}
          >
            <Search className="w-5 h-5 text-indigo-400 mr-3 shrink-0" />
            <input
              ref={inputRef}
              type="text"
              value={query || (selectedVendor ? selectedVendor : selectedCategory)}
              onChange={(e) => {
                setQuery(e.target.value);
                setIsOpen(true);
              }}
              onFocus={() => {
                setIsOpen(true);
                if (selectedVendor || selectedCategory) setQuery('');
              }}
              placeholder="Search merchant, app, or category (e.g. Swiggy, Amazon, Flights)..."
              className="w-full bg-transparent text-sm sm:text-base text-white placeholder-slate-500 focus:outline-none font-medium"
            />

            {/* Clear or Keyboard Shortcut Indicator */}
            <div className="flex items-center space-x-2 shrink-0 ml-2">
              {query || selectedVendor ? (
                <button
                  type="button"
                  onClick={handleClear}
                  className="p-1 rounded-full text-slate-400 hover:text-white hover:bg-white/10 transition"
                  title="Clear search"
                >
                  <X className="w-4 h-4" />
                </button>
              ) : (
                <kbd className="hidden sm:inline-flex items-center px-2 py-0.5 text-[10px] font-mono text-slate-400 bg-white/5 border border-white/10 rounded">
                  ⌘K
                </kbd>
              )}
            </div>
          </div>

          {/* Autocomplete Dropdown */}
          {isOpen && (
            <div className="absolute left-0 right-0 top-full mt-2 z-50 rounded-2xl bg-obsidian-850/95 backdrop-blur-2xl border border-white/15 shadow-2xl overflow-hidden max-h-96 overflow-y-auto">
              {/* Category Matches */}
              {filteredCategories.length > 0 && (
                <div className="p-2 border-b border-white/10">
                  <div className="text-[10px] font-bold text-slate-400 uppercase tracking-wider px-3 py-1">
                    Categories
                  </div>
                  {filteredCategories.map(cat => (
                    <button
                      key={cat}
                      type="button"
                      onClick={() => handlePickCategory(cat)}
                      className="w-full flex items-center justify-between px-3 py-2 text-sm text-slate-200 hover:bg-white/10 rounded-xl transition text-left"
                    >
                      <span className="flex items-center space-x-2">
                        <span>{CATEGORY_ICONS[cat] || '📂'}</span>
                        <span className="font-semibold text-white">{cat}</span>
                      </span>
                      <span className="text-xs text-indigo-400 flex items-center">
                        Select Category <ArrowRight className="w-3 h-3 ml-1" />
                      </span>
                    </button>
                  ))}
                </div>
              )}

              {/* Merchant Matches */}
              <div className="p-2">
                <div className="text-[10px] font-bold text-slate-400 uppercase tracking-wider px-3 py-1 flex justify-between">
                  <span>Merchant Partners</span>
                  <span>Max Cashback</span>
                </div>
                {filteredMerchants.length === 0 ? (
                  <div className="px-4 py-6 text-center text-xs text-slate-400">
                    No partner found for "{query}". You can still calculate based on general category.
                  </div>
                ) : (
                  filteredMerchants.slice(0, 10).map(([name, data]) => (
                    <button
                      key={name}
                      type="button"
                      onClick={() => handlePickMerchant(name, data.category)}
                      className="w-full flex items-center justify-between px-3 py-2.5 hover:bg-white/10 rounded-xl transition text-left group"
                    >
                      <div className="flex items-center space-x-3">
                        <span className="text-xl p-1.5 rounded-lg bg-white/5 border border-white/10 group-hover:scale-110 transition">
                          {data.icon}
                        </span>
                        <div>
                          <div className="font-semibold text-white text-sm flex items-center gap-2">
                            {name}
                            <span className="text-[10px] font-normal px-2 py-0.5 rounded-full bg-white/5 text-slate-400">
                              {data.category}
                            </span>
                          </div>
                          <p className="text-[11px] text-slate-400 line-clamp-1">{data.description}</p>
                        </div>
                      </div>

                      <div className="text-right shrink-0">
                        <span className="px-2.5 py-1 rounded-full bg-emerald-500/15 border border-emerald-500/30 text-emerald-400 text-xs font-bold font-mono">
                          Up to {data.max_potential_rate}%
                        </span>
                      </div>
                    </button>
                  ))
                )}
              </div>
            </div>
          )}
        </div>

        {/* Spend Amount Input (4 Cols) */}
        <div className="md:col-span-4 relative">
          <div className="relative flex items-center bg-obsidian-800 border border-white/10 hover:border-white/20 rounded-2xl px-4 py-3.5 transition focus-within:border-emerald-500 focus-within:ring-2 focus-within:ring-emerald-500/20">
            <span className="text-slate-400 font-mono text-lg font-bold mr-2">₹</span>
            <input
              type="number"
              min={100}
              max={2000000}
              step={500}
              value={amount || ''}
              onChange={(e) => onAmountChange(Number(e.target.value) || 0)}
              className="w-full bg-transparent text-lg sm:text-xl font-bold font-mono text-white focus:outline-none"
              placeholder="5,000"
            />
            <div className="text-[10px] text-slate-400 uppercase font-semibold tracking-wider shrink-0 bg-white/5 px-2 py-1 rounded">
              Purchase
            </div>
          </div>
        </div>
      </div>

      {/* Quick Merchant Chips */}
      <div className="flex items-center space-x-2 overflow-x-auto pb-1 text-xs no-scrollbar">
        <span className="text-slate-500 text-[11px] font-medium shrink-0 flex items-center gap-1">
          <Sparkles className="w-3 h-3 text-indigo-400" /> Popular:
        </span>
        {popularQuickPicks.map((pick) => {
          const isActive = selectedVendor === pick.vendor;
          return (
            <button
              key={pick.label}
              type="button"
              onClick={() => handlePickMerchant(pick.vendor, pick.category)}
              className={`px-3 py-1.5 rounded-full flex items-center space-x-1.5 shrink-0 transition font-medium text-xs ${
                isActive
                  ? 'bg-indigo-600 text-white shadow-glow-indigo border border-indigo-400/50'
                  : 'bg-obsidian-800 border border-white/10 text-slate-300 hover:border-white/25 hover:text-white'
              }`}
            >
              <span>{pick.icon}</span>
              <span>{pick.label}</span>
            </button>
          );
        })}
      </div>
    </div>
  );
};
