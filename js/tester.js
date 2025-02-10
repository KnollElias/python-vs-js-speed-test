const axios = require('axios');

const url = 'http://127.0.0.1:8000/';

async function benchmark() {
    const start = Date.now();
    for (let i = 0; i < 1000; i++) {
        await axios.get(url);
    }
    const end = Date.now();
    console.log(`Total time for 1000 requests: ${(end - start) / 1000} seconds`);
}

benchmark();
