const express = require('express');
const { ReclaimClient } = require('@reclaimprotocol/zk-fetch');

const app = express();
const PORT = 3000;

const client = new ReclaimClient(
  '0x0074eC594b8cAfa7A0bFF9C2577CcFE6a70A042f',
  '0xaf0646ecac92cd35c14996494e5bd5c7595f4f3932ac13b9bd8fb3375eadc52e'
);

app.get('/fetch-proof', async (req, res) => {
  const publicOptions = {
    method: 'GET',
    headers: {
      accept: 'application/json, text/plain, */*'
    }
  };
  try {
    const proof = await client.zkFetch(
      'https://api.opendota.com/api/proMatches',
      publicOptions
    );
    res.json(proof);
  } catch (error) {
    res.status(500).send({ error: error.message });
  }
});

app.listen(PORT, () => {
  console.log(`Middleware service running at http://localhost:${PORT}`);
});
