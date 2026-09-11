import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { Wifi, Sparkles, Info, Check, ShieldCheck } from 'lucide-react';
import { CARDS_DATABASE, CreditCardData } from '../lib/data';

interface CreditCardSkinProps {
  cardName: string;
  isSelected?: boolean;
  onToggleSelect?: (cardName: string) => void;
  showSpendCap?: boolean;
  spendCapRemaining?: number;
  totalCap?: number;
  highlightWinning?: boolean;
  size?: 'sm' | 'md' | 'lg';
}

export const CreditCardSkin: React.FC<CreditCardSkinProps> = ({
  cardName,
  isSelected = true,
  onToggleSelect,
  showSpendCap = false,
  spendCapRemaining,
  totalCap,
  highlightWinning = false,
  size = 'md'
}) => {
  const [isFlipped, setIsFlipped] = useState(false);
  const [rotateX, setRotateX] = useState(0);
  const [rotateY, setRotateY] = useState(0);

  const card: CreditCardData | undefined = CARDS_DATABASE[cardName];
  if (!card) {
    return (
      <div className="p-4 rounded-xl bg-obsidian-800 border border-white/10 text-slate-400 text-xs">
        Card: {cardName}
      </div>
    );
  }

  const skin = card.skin;

  const handleMouseMove = (e: React.MouseEvent<HTMLDivElement>) => {
    if (isFlipped) return;
    const rect = e.currentTarget.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    const centerX = rect.width / 2;
    const centerY = rect.height / 2;
    const rotX = ((y - centerY) / centerY) * -10;
    const rotY = ((x - centerX) / centerX) * 10;
    setRotateX(rotX);
    setRotateY(rotY);
  };

  const handleMouseLeave = () => {
    setRotateX(0);
    setRotateY(0);
  };

  const sizeClasses = {
    sm: 'w-64 h-40 text-xs',
    md: 'w-72 h-44 sm:w-80 sm:h-48 text-sm',
    lg: 'w-84 h-52 sm:w-96 sm:h-56 text-base',
  }[size];

  // Render Network Logo
  const renderNetworkLogo = () => {
    const net = card.network.toLowerCase();
    if (net.includes('visa')) {
      return (
        <span className="font-extrabold italic tracking-wider text-white text-xs sm:text-sm drop-shadow-md">
          VISA <span className="text-[10px] font-normal not-italic opacity-80">{card.network.replace('Visa', '').trim()}</span>
        </span>
      );
    }
    if (net.includes('mastercard')) {
      return (
        <div className="flex items-center -space-x-1.5">
          <div className="w-4 h-4 sm:w-5 sm:h-5 rounded-full bg-red-600 opacity-90 shadow-sm" />
          <div className="w-4 h-4 sm:w-5 sm:h-5 rounded-full bg-amber-500 opacity-90 shadow-sm" />
        </div>
      );
    }
    if (net.includes('rupay')) {
      return (
        <div className="flex items-center space-x-1 font-black italic tracking-tighter text-white text-xs">
          <span className="text-orange-500">Ru</span><span className="text-emerald-400">Pay</span>
          <span className="text-[9px] not-italic text-slate-300 font-normal">Select</span>
        </div>
      );
    }
    if (net.includes('american express') || net.includes('amex')) {
      return (
        <div className="px-1.5 py-0.5 rounded bg-blue-600/60 border border-blue-400/40 text-[10px] font-bold text-white tracking-wider">
          AMEX
        </div>
      );
    }
    if (net.includes('diners')) {
      return (
        <div className="w-5 h-5 rounded-full border-2 border-sky-400 flex items-center justify-center text-[10px] font-bold text-sky-300">
          D
        </div>
      );
    }
    return <span className="text-xs font-semibold text-white/80">{card.network}</span>;
  };

  return (
    <div className="relative group perspective-1000 select-none">
      {/* Glow Halo if Winning Card */}
      {highlightWinning && (
        <div className="absolute -inset-1.5 bg-gradient-to-r from-emerald-500 to-teal-400 rounded-3xl blur-md opacity-70 group-hover:opacity-100 transition duration-500 animate-pulse-subtle" />
      )}

      {/* Card Wrapper with 3D Tilt */}
      <motion.div
        onMouseMove={handleMouseMove}
        onMouseLeave={handleMouseLeave}
        animate={{
          rotateX: isFlipped ? 0 : rotateX,
          rotateY: isFlipped ? 180 : rotateY,
        }}
        transition={{ type: 'spring', stiffness: 300, damping: 20 }}
        style={{ transformStyle: 'preserve-3d' }}
        className={`relative ${sizeClasses} rounded-2xl cursor-pointer transition-shadow duration-300 shadow-2xl ${
          highlightWinning ? 'ring-2 ring-emerald-400' : 'hover:shadow-glow-indigo'
        }`}
      >
        {/* FRONT FACE */}
        <div
          className={`absolute inset-0 rounded-2xl p-4 sm:p-5 flex flex-col justify-between overflow-hidden backface-hidden border border-white/15`}
          style={{ background: skin.gradient }}
        >
          {/* Subtle Ambient Sheen / Grid Pattern */}
          <div className="absolute inset-0 bg-[radial-gradient(circle_at_20%_20%,rgba(255,255,255,0.18)_0%,transparent_50%)] pointer-events-none" />
          <div className="absolute -right-8 -bottom-8 w-36 h-36 rounded-full bg-white/5 blur-xl pointer-events-none" />

          {/* Top Bar: Bank Name, Contactless Icon, and Action Toggle */}
          <div className="relative z-10 flex items-center justify-between">
            <div className="flex items-center space-x-2">
              <span className="font-extrabold tracking-tight text-white/95 uppercase text-[11px] sm:text-xs">
                {card.bank}
              </span>
              <Wifi className="w-3.5 h-3.5 text-white/60 rotate-90" />
            </div>

            <div className="flex items-center space-x-2">
              {/* Badge */}
              <span className="px-2 py-0.5 rounded-full text-[9px] font-bold tracking-wide uppercase bg-black/40 border border-white/20 backdrop-blur-md"
                style={{ color: skin.accentColor }}>
                {skin.badge}
              </span>

              {/* Wallet Select Checkbox if enabled */}
              {onToggleSelect && (
                <button
                  type="button"
                  onClick={(e) => {
                    e.stopPropagation();
                    onToggleSelect(cardName);
                  }}
                  className={`w-5 h-5 rounded-full flex items-center justify-center transition-all ${
                    isSelected
                      ? 'bg-emerald-500 text-black shadow-glow-emerald'
                      : 'bg-black/60 border border-white/30 text-transparent hover:border-white/60'
                  }`}
                  title={isSelected ? "In your wallet" : "Add to wallet"}
                >
                  <Check className="w-3 h-3 stroke-[3]" />
                </button>
              )}
            </div>
          </div>

          {/* Middle Bar: EMV Chip & Card Nickname */}
          <div className="relative z-10 my-auto flex items-center justify-between">
            {/* Realistic EMV Chip */}
            <div className="w-10 h-7 rounded-md bg-gradient-to-br from-amber-200 via-amber-400 to-amber-600 p-0.5 shadow-md flex items-center justify-center border border-amber-300/40">
              <div className="w-full h-full rounded-[3px] border border-amber-700/30 grid grid-cols-3 grid-rows-2 gap-0.5 p-0.5 opacity-85">
                <div className="border border-amber-900/30 rounded-[1px]" />
                <div className="border border-amber-900/30 rounded-[1px] col-span-2" />
                <div className="border border-amber-900/30 rounded-[1px] col-span-2" />
                <div className="border border-amber-900/30 rounded-[1px]" />
              </div>
            </div>

            {/* Quick Flip Info Button */}
            <button
              type="button"
              onClick={(e) => {
                e.stopPropagation();
                setIsFlipped(true);
              }}
              className="p-1 rounded-full bg-white/10 hover:bg-white/20 text-white/70 hover:text-white transition"
              title="View Card Rules & Perks"
            >
              <Info className="w-3.5 h-3.5" />
            </button>
          </div>

          {/* Bottom Bar: Card Title, Spend Cap / Feature Tag, and Network Logo */}
          <div className="relative z-10 space-y-1.5">
            <div className="flex items-end justify-between">
              <div>
                <h4 className="font-bold text-white tracking-wide text-xs sm:text-sm drop-shadow-sm line-clamp-1">
                  {card.name}
                </h4>
                <p className="text-[10px] sm:text-[11px] text-white/75 font-medium tracking-tight">
                  {skin.tagline}
                </p>
              </div>

              <div>{renderNetworkLogo()}</div>
            </div>

            {/* Spend Cap Bar if applicable */}
            {showSpendCap && totalCap && spendCapRemaining !== undefined && (
              <div className="pt-1">
                <div className="flex justify-between text-[9px] text-white/80 font-mono mb-0.5">
                  <span>Cap Remaining: ₹{spendCapRemaining.toLocaleString()}</span>
                  <span>Max ₹{totalCap.toLocaleString()}</span>
                </div>
                <div className="w-full h-1 rounded-full bg-black/40 overflow-hidden">
                  <div
                    className="h-full rounded-full bg-emerald-400 transition-all duration-500"
                    style={{ width: `${Math.max(5, Math.min(100, (spendCapRemaining / totalCap) * 100))}%` }}
                  />
                </div>
              </div>
            )}
          </div>
        </div>

        {/* BACK FACE (Details, Lounge, Forex, Fee) */}
        <div
          className={`absolute inset-0 rounded-2xl p-4 sm:p-5 flex flex-col justify-between overflow-hidden backface-hidden rotate-y-180 bg-obsidian-850 border border-white/15`}
        >
          <div className="flex items-center justify-between pb-2 border-b border-white/10">
            <div className="flex items-center space-x-1.5">
              <ShieldCheck className="w-4 h-4 text-emerald-400" />
              <span className="text-xs font-bold text-white">{card.name} Details</span>
            </div>
            <button
              type="button"
              onClick={(e) => {
                e.stopPropagation();
                setIsFlipped(false);
              }}
              className="text-[10px] text-indigo-400 hover:text-indigo-300 font-semibold uppercase tracking-wider"
            >
              Flip Back ↺
            </button>
          </div>

          <div className="space-y-1.5 text-[11px] text-slate-300">
            <div className="flex justify-between">
              <span className="text-slate-400">Annual Fee:</span>
              <span className="font-mono font-semibold text-white">
                {card.annual_fee === 0 ? '₹0 (Lifetime Free)' : `₹${card.annual_fee.toLocaleString()}`}
              </span>
            </div>
            {card.fee_waiver_spend > 0 && (
              <div className="flex justify-between">
                <span className="text-slate-400">Waiver Target:</span>
                <span className="font-mono text-amber-300">₹{card.fee_waiver_spend.toLocaleString()}/yr</span>
              </div>
            )}
            <div className="flex justify-between">
              <span className="text-slate-400">Forex Markup:</span>
              <span className={`font-mono ${card.forex_markup === 0 ? 'text-emerald-400 font-bold' : 'text-slate-300'}`}>
                {card.forex_markup}%
              </span>
            </div>
            <div className="flex justify-between">
              <span className="text-slate-400">Domestic Lounge:</span>
              <span className="text-slate-200 truncate max-w-[150px] text-right" title={card.domestic_lounges}>
                {card.domestic_lounges}
              </span>
            </div>
          </div>

          <div className="pt-2 border-t border-white/10 flex items-center justify-between">
            <span className="text-[10px] text-slate-400 capitalize">{card.tier} Tier</span>
            <a
              href={card.apply_url}
              target="_blank"
              rel="noopener noreferrer"
              onClick={(e) => e.stopPropagation()}
              className="text-[10px] px-2.5 py-1 rounded-md bg-white/10 hover:bg-white/20 text-white font-medium transition"
            >
              Apply Page ↗
            </a>
          </div>
        </div>
      </motion.div>
    </div>
  );
};
