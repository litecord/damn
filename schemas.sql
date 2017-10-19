CREATE TABLE users (
    id text PRIMARY KEY NOT NULL,
    discriminator varchar(4) NOT NULL,
    avatar text,
    bot boolean DEFAULT FALSE,
    mfa_enabled boolean DEFAULT FALSE,
    flags int DEFAULT 0,
    verified boolean DEFAULT FALSE,
    email varchar(255) NOT NULL,
    phone varchar(60) DEFAULT '',

    password_hash text NOT NULL,
    password_salt text NOT NULL,
);

CREATE TABLE guilds (
    id text PRIMARY KEY NOT NULL,
    name varchar(255) NOT NULL, /* TODO: max guild name size */
    owner_id text NOT NULL,
    region text NOT NULL,
    features text, /* JSON encoded data, like "[\"VANITY_URL\"]" */
    icon text,
);

CREATE TABLE members (
    hash text PRIMARY KEY NOT NULL,
    user_id text NOT NULL,
    guild_id text NOT NULL,
    nickname varchar(100),
);

CREATE TABLE channels (
    id text PRIMARY KEY NOT NULL,
    guild_id text NOT NULL,
    channel_type int NOT NULL,
    name varchar(255) NOT NULL,
    position int NOT NULL,
    topic varchar(1024),
);

CREATE TABLE roles (
    id text PRIMARY KEY NOT NULL
    guild_id text NOT NULL,
    position int NOT NULL,
    permissions int NOT NULL,
);

CREATE TABLE bans (
    hash text PRIMARY KEY NOT NULL
    user_id text NOT NULL,
    guild_id text NOT NULL,
    reason varchar(500),
);
