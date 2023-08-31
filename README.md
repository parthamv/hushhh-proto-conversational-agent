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

5. Uploading the json and csv files of Instagram and twitter to Pinecone vector database after converting them to vector embeddings using OpenAI embeddings

```
python vector_store.py
```
6. The design document is available i the GitHub repository as HUSH PROTO.docx
