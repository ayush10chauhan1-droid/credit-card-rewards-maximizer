import React, { useState, useEffect } from 'react';
import { Search, BookOpen, AlertTriangle, ShieldCheck, HelpCircle } from 'lucide-react';

interface RuleDoc {
  card: string;
  topic: string;
  text: string;
  score?: number;
}

const FALLBACK_RULES: RuleDoc[] = [
  {
    card: "SBI Cashback Card",
    topic: "Capping & Exclusions",
    text: "Flat 5% cashback on online transactions capped at ₹5,000 per billing cycle (on ₹1,00,000 spend). Excludes rent, fuel, utility bills, wallet loads, jewelry, insurance, and school fees."
  },
  {
    card: "Swiggy HDFC",
    topic: "Monthly Cashback Caps",
    text: "10% cashback on Swiggy App (Food, Instamart, Dineout, Genie) capped at ₹1,500/month. 5% cashback on online merchants capped at ₹1,500/month. Total max monthly cashback: ₹3,000."
  },
  {
    card: "HDFC Millennia",
    topic: "SmartBuy & Partner Caps",
    text: "5% cashback on Amazon, Flipkart, Swiggy, Zomato, Uber, BookMyShow, Myntra, Tata CLiQ, Cult.fit, and Sony LIV. Capped at ₹1,000 CashPoints per calendar month."
  },
  {
    card: "Axis Ace",
    topic: "Google Pay Utilities Cap",
    text: "5% cashback on utility bill payments (electricity, gas, water, broadband) made via Google Pay Android app. Capped at ₹500 cashback per billing cycle (₹10,000 spend)."
  },
  {
    card: "Airtel Axis",
    topic: "25% Airtel & 10% Utility Rules",
    text: "25% cashback on Airtel Mobile, Broadband & DTH recharges capped at ₹250/mo. 10% on electricity, gas, water bills via Airtel Thanks capped at ₹250/mo. 10% on Swiggy, Zomato, BigBasket capped at ₹500/mo."
  },
  {
    card: "HDFC Infinia Metal",
    topic: "SmartBuy 10x / Accelerated Capping",
    text: "Earn up to 33% value back on hotels and 16.5% on flight tickets via SmartBuy. Daily accelerated cap: 7,500 points. Monthly accelerated cap: 10,000 points. 1 Reward Point = ₹1."
  }
];

export const RAGKnowledgeHub: React.FC = () => {
  const [query, setQuery] = useState('capping');
  const [docs, setDocs] = useState<RuleDoc[]>(FALLBACK_RULES);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const fetchRules = async () => {
      setLoading(true);
      try {
        const res = await fetch(`http://localhost:8000/api/rules?q=${encodeURIComponent(query)}&top_k=6`);
        if (res.ok) {
          const data = await res.json();
          if (data.docs && data.docs.length > 0) {
            setDocs(data.docs);
            setLoading(false);
            return;
          }
        }
      } catch {
        // Fallback filter
      }

      // Local fallback filter
      const filtered = FALLBACK_RULES.filter(
        d => d.card.toLowerCase().includes(query.toLowerCase()) ||
             d.topic.toLowerCase().includes(query.toLowerCase()) ||
             d.text.toLowerCase().includes(query.toLowerCase())
      );
      setDocs(filtered.length > 0 ? filtered : FALLBACK_RULES);
      setLoading(false);
    };

    const debounce = setTimeout(fetchRules, 250);
    return () => clearTimeout(debounce);
  }, [query]);

  return (
    <div className="space-y-6">
      {/* Search Header */}
      <div className="p-6 sm:p-8 rounded-3xl bg-obsidian-800 border border-white/10 space-y-4">
        <div className="flex items-center space-x-2.5">
          <BookOpen className="w-5 h-5 text-indigo-400" />
          <h2 className="text-xl sm:text-2xl font-extrabold text-white tracking-tight">
            Card Rules & RAG Knowledge Hub
          </h2>
        </div>
        <p className="text-xs text-slate-400">
          Search official bank terms, monthly capping limits, lounge access criteria, fuel surcharge waivers, and exclusions.
        </p>

        {/* Search Input */}
        <div className="relative">
          <Search className="w-5 h-5 text-slate-400 absolute left-4 top-1/2 -translate-y-1/2" />
          <input
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Search rules (e.g. 'capping', 'lounge access', 'fuel waiver', 'SmartBuy')..."
            className="w-full bg-obsidian-750 border border-white/10 hover:border-white/20 focus:border-indigo-500 rounded-2xl pl-12 pr-4 py-3.5 text-sm text-white placeholder-slate-500 focus:outline-none transition"
          />
        </div>
      </div>

      {/* Results Grid */}
      <div className="space-y-3">
        <span className="text-xs font-bold text-slate-400 uppercase tracking-wider block">
          Retrieved Documents ({docs.length})
        </span>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {docs.map((doc, idx) => (
            <div
              key={idx}
              className="p-5 rounded-2xl bg-obsidian-800 border border-white/10 space-y-2 hover:border-white/20 transition"
            >
              <div className="flex justify-between items-center">
                <span className="font-bold text-sm text-emerald-400">{doc.card}</span>
                <span className="px-2.5 py-0.5 rounded-full text-[10px] font-bold uppercase tracking-wider bg-indigo-500/10 text-indigo-300 border border-indigo-500/20">
                  {doc.topic}
                </span>
              </div>
              <p className="text-xs text-slate-300 leading-relaxed">
                {doc.text}
              </p>
            </div>
          ))}
        </div>
      </div>

      {/* Universal Exclusions Warning Box */}
      <div className="p-6 rounded-3xl bg-obsidian-800 border border-white/10 space-y-4">
        <div className="flex items-center space-x-2 text-amber-400 font-bold text-sm">
          <AlertTriangle className="w-4 h-4" />
          <span>Universal Indian Credit Card Exclusions (2026 RBI Guidelines)</span>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3 text-xs text-slate-300">
          <div className="p-4 rounded-2xl bg-obsidian-850 border border-white/5 space-y-1">
            <span className="font-bold text-white block">Wallet Reloads</span>
            <p className="text-slate-400 text-[11px]">Paytm, Amazon Pay, or Mobikwik loads incur 1% to 2.5% surcharge and 0 reward points.</p>
          </div>

          <div className="p-4 rounded-2xl bg-obsidian-850 border border-white/5 space-y-1">
            <span className="font-bold text-white block">Rent Payments</span>
            <p className="text-slate-400 text-[11px]">CRED, Magicbricks, or Paytm rent payments incur 1% fee + 18% GST with zero rewards across issuers.</p>
          </div>

          <div className="p-4 rounded-2xl bg-obsidian-850 border border-white/5 space-y-1">
            <span className="font-bold text-white block">Fuel Surcharge</span>
            <p className="text-slate-400 text-[11px]">Exempt from standard rewards; eligible for 1% surcharge waiver on ₹400–₹4,000 transactions.</p>
          </div>

          <div className="p-4 rounded-2xl bg-obsidian-850 border border-white/5 space-y-1">
            <span className="font-bold text-white block">Govt & Tax Payments</span>
            <p className="text-slate-400 text-[11px]">Advance tax, property tax, and municipal fees are universally excluded from reward programs.</p>
          </div>
        </div>
      </div>
    </div>
  );
};
