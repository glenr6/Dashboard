import React from 'react';

function TokenList() {
  // This would be fetched from the backend, possibly via a context or Redux store
  const tokens = [
    { symbol: 'BTC', price: '48000', change: '3.5%' },
    { symbol: 'ETH', price: '3200', change: '2.1%' },
    // ...other tokens
  ];

  return (
    <div className="TokenList">
      {tokens.map(token => (
        <div key={token.symbol} className="Token">
          <span>{token.symbol}</span>
          <span>{token.price}</span>
          <span>{token.change}</span>
        </div>
      ))}
    </div>
  );
}

export default TokenList;
