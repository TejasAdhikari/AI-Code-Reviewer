CREATE TABLE code_reviews (
    id SERIAL PRIMARY KEY,
    code TEXT NOT NULL,
    feedback TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
