# System Design Practice Roadmap

## Tier 1 — Fundamentals (must know)
- [ ] **URL Shortener (TinyURL, bit.ly)** – Hash functions, DB sharding, cache 
- [ ] **Rate Limiter (API gateway)** – Sliding window, leaky bucket, Redis
- [ ] **Key-Value Store (Redis)** – In-memory storage, eviction, persistence

## Tier 2 — Core Social & Messaging Systems
- [ ] **Twitter / News Feed** – Fanout (push vs pull), caching, denormalization  
- [ ] **Instagram / Facebook** – Photo storage (CDN, blob), timelines, metadata indexing  
- [ ] **WhatsApp / Messenger (Chat)** – Pub/Sub, delivery guarantees, read receipts  
- [ ] **Notification System** – Fanout, retries, prioritization  

## Tier 3 — Content & Search
- [ ] **YouTube / Netflix (Video Streaming)** – CDN, chunking, adaptive bitrate streaming  
- [ ] **Google Search Autocomplete** – Tries, prefix search, caching, ranking  
- [ ] **Web Crawler** – Distributed crawling, deduplication, politeness  
- [ ] **Search Engine (high level)** – Inverted index, ranking, crawling pipeline  

## Tier 4 — Distributed Infra & Storage
- [ ] **Dropbox / Google Drive (File Storage)** – Consistency, chunking, syncing, metadata service  
- [ ] **Distributed Cache (Memcached)** – Consistent hashing, replication, invalidation  
- [ ] **Pub/Sub System (Kafka)** – Log-based storage, partitioning, consumer groups  
- [ ] **Distributed Database (DynamoDB, Bigtable)** – Partitioning, replication, CAP tradeoffs  

## Tier 5 — Advanced / Niche Systems
- [ ] **Payment System (Stripe)** – Idempotency, fraud detection, consistency  
- [ ] **Ride-Sharing (Uber, Lyft)** – Real-time matching, geospatial indexing, surge pricing  
- [ ] **Metrics/Monitoring (Prometheus, Datadog)** – Time-series DB, high-ingest rate, rollups  
- [ ] **Ad System (Google Ads)** – Auctions, ranking, targeting, fraud prevention  
- [ ] **IoT Platform** – Device constraints, real-time ingestion, MQTT/Kafka  

## Suggested Practice Path
1. **Tier 1** → URL Shortener → Rate Limiter → KV Store  
2. **Tier 2** → Twitter → Instagram → Chat → Notifications  
3. **Tier 3** → YouTube → Autocomplete → Crawler → Search  
4. **Tier 4** → Dropbox → Cache → Kafka → DynamoDB  
5. **Tier 5** → Payments → Uber → Monitoring → Ads → IoT  

## How to Practice Each System
For every system you design:
- Define **requirements** (functional + non-functional)  
- Draft **APIs** (CRUD, queries, basic endpoints)  
- Sketch a **high-level design** (components: LB, cache, DB, queue)  
- Identify **bottlenecks** (hot keys, scale, consistency, failover)  
- Discuss **tradeoffs** (latency vs consistency, SQL vs NoSQL, push vs pull)  
