import axios from "axios";

const api = "http://127.0.0.1:5000";

export const getCurrencies = async () => {
  return axios.get<string[]>(`${api}`);
};

export const convertCurrency = async (
  origin: string,
  destiny: string,
  amount: number
) => {
  return axios.post<{ result: number }>(`${api}/convert`, {
    origin,
    destiny,
    amount,
  });
};