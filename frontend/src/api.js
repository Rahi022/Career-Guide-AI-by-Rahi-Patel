import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:8000",
});

export const getCareerAdvice = async (message) => {
  const response = await API.post("/career", {
    message: message,
  });
  return response.data;
};
