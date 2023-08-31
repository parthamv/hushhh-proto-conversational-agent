Install packages

```
npm install
```

3. Set up your `.env` file

- Change `.env.example` into `.env` and fill the neccessary keys.
- For OPENAI API key visit [openai](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key)
- For Pinecone API key and environment and index names visit [pinecone](https://pinecone.io/) and create your index

4. Run the development server:

```
npm run dev
```

5. Uploading the json and csv files of instagram and twitter to pinecone vector database after converting it to vector embeddings using OpenAI embeddings

use and run vector_store.py
