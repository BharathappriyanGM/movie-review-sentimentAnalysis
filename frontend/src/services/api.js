import axios from "axios";

// Set the base URL for API calls
const instance = axios.create({
    baseURL: "http://localhost:8000",
    timeout: 5000 // Timeout after 5 seconds
});


export default instance;
