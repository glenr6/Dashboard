const API_BASE_URL = 'http://localhost:5000'; // Backend API URL

export const fetchMarketData = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/market-data`);
    if (!response.ok) throw new Error('Network response was not ok');
    return await response.json();
  } catch (error) {
    console.error('Error fetching market data:', error);
  }
};

// Add more API call functions as needed
