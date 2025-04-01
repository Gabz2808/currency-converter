import React, { useEffect, useState } from "react";
import * as CurrencyService from "../../services/GoRestService";

export const Home: React.FC = () => {
  const [currencies, setCurrencies] = useState<string[]>([]);
  const [originCurrency, setOriginCurrency] = useState<string>("");
  const [destinyCurrency, setDestinyCurrency] = useState<string>("");
  const [amount, setAmount] = useState<number>(0);
  const [result, setResult] = useState<number | null>(null);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    getCurrenciesList();
  }, []);

  const getCurrenciesList = async () => {
    setLoading(true);
    setError(null);
    try {
      const res = await CurrencyService.getCurrencies();
      console.log("API Response:", res);
      setCurrencies(res);
    } catch (err) {
      console.error("Error fetching currencies:", err);
      setError("Failed to load currencies.");
    } finally {
      setLoading(false);
    }
  };

  const handleConvert = async () => {
    if (!originCurrency || !destinyCurrency || amount <= 0) {
      setError("Please fill all fields and enter a valid amount.");
      return;
    }

    setError(null);
    setLoading(true);

    try {
      const res = await CurrencyService.convertCurrency(
        originCurrency,
        destinyCurrency,
        amount
      );
      if (res.data?.result) {
        setResult(res.data.result);
      } else {
        throw new Error("Invalid response from server");
      }
    } catch (err) {
      console.error("Error converting currency:", err);
      setError("Error converting currencies.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex items-center justify-center h-screen">
      <div className="max-w-sm rounded overflow-hidden shadow-lg text-black font-bold border p-10">
        <div className="font-bold text-xl mb-4 text-center">
          Currency Converter
        </div>

        {loading && <p className="text-center text-blue-500">Loading...</p>}
        {error && <p className="text-center text-red-500">{error}</p>}

        <div className="flex flex-col space-y-4">
          <select
            id="origin"
            className="py-2 px-4 rounded"
            value={originCurrency}
            onChange={(e) => setOriginCurrency(e.target.value)}
          >
            <option value="">Select Origin</option>
            {currencies.map((currency) => (
              <option key={currency} value={currency}>
                {currency}
              </option>
            ))}
          </select>

          <select
            id="destiny"
            className="py-2 px-4 rounded"
            value={destinyCurrency}
            onChange={(e) => setDestinyCurrency(e.target.value)}
          >
            <option value="">Select Destiny</option>
            {currencies.map((currency) => (
              <option key={currency} value={currency}>
                {currency}
              </option>
            ))}
          </select>

          <input
            type="number"
            id="amount"
            placeholder="Amount"
            className="py-2 px-4 rounded"
            value={amount}
            onChange={(e) => setAmount(parseFloat(e.target.value) || 0)}
          />

          <button
            className="bg-blue-500 transition delay-150 duration-300 ease-in-out hover:-translate-y-1 hover:scale-110 hover:bg-indigo-500 py-2 px-4 rounded text-white"
            onClick={handleConvert}
          >
            Convert
          </button>

          <div className="text-center mt-4">
            {result !== null ? (
              <p>Converted Amount: {result.toFixed(2)}</p>
            ) : (
              <p>Please enter the amount and select currencies to convert.</p>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};
