-- ------------
-- Social Media API : Articuno Coding LLP
-- SQL Codes
-- ------------

-- ------------
-- Database: Social
-- ------------
-- For creating postgres db, use command line
-- postgres=#  createdb social;

-- ------------
-- DROP TABLES IF EXISTS
-- ------------
DROP TABLE IF EXISTS likes;
DROP TABLE IF EXISTS messages;


-- ------------
-- TABLE: MESSEAGES
-- ------------
CREATE TABLE messages (
    id          SERIAL      NOT NULL,
    "user_id"   INTEGER     NOT NULL,
    "message"   TEXT        NOT NULL,
    "likes"     INTEGER     DEFAULT 0,
    "timestamp" TIMESTAMP   DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT messages_pkey PRIMARY KEY (id)
);


-- ------------
-- TABLE: LIKES
-- ------------
CREATE TABLE IF NOT EXISTS public.likes
(
    "message_id"  INTEGER NOT NULL,
    "user_id"     INTEGER NOT NULL,
    CONSTRAINT likes_pkey            PRIMARY KEY (message_id, user_id),
    CONSTRAINT likes_message_id_fkey FOREIGN KEY (message_id)
    REFERENCES messages (id) MATCH SIMPLE
);


-- ------------
-- INDEXING
-- ------------
CREATE INDEX idx_message ON messages(id);
CREATE INDEX idx_likes ON likes(message_id, user_id);


-- ------------
-- TRIGGER
-- ------------
CREATE FUNCTION updateLikesCount()
RETURNS TRIGGER
AS
$$
BEGIN
	IF (TG_OP = 'INSERT') THEN
		UPDATE messages SET likes = likes + 1 WHERE id = NEW.message_id;
	ELSEIF (TG_OP = 'DELETE') THEN
		UPDATE messages SET likes = likes - 1 WHERE id = OLD.message_id;
	END IF;
	RETURN OLD;
END
$$
LANGUAGE plpgsql;

CREATE TRIGGER updateLikesCount 
AFTER INSERT OR DELETE ON likes
FOR EACH ROW
EXECUTE PROCEDURE updateLikesCount();

