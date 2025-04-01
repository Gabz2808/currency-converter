import axios from "axios";

const api = "http://127.0.0.1:5000";

interface CurrencyRates {
  [currencyCode: string]: number;
}

export const getCurrencies = async (): Promise<string[]> => {
  const response = await axios.get<CurrencyRates>(`${api}/`);
  return Object.keys(response.data); 
};

export const convertCurrency = async (
  origin: string,
  destiny: string,
  amount: number
) => {
  return axios.post<{ result: number }>(`${api}/convert`, { origin, destiny, amount });
};