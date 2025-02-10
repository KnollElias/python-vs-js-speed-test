const express = require('express');
const app = express();

app.get('/', (req, res) => {
    const start = Date.now();
    res.json({ response: "Hello from Express", time_taken: Date.now() - start });
});

app.listen(8000, () => {
    console.log('Server running on http://127.0.0.1:8000');
});
