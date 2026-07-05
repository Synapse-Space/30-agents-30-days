CREATE TABLE IF NOT EXISTS memories (

    id UUID PRIMARY KEY,

    user_id TEXT NOT NULL,

    key TEXT NOT NULL,

    value TEXT NOT NULL,

    created_at TIMESTAMP NOT NULL

);

CREATE INDEX idx_user
ON memories(user_id);