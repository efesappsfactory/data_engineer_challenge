CREATE OR REPLACE TABLE departments (
    id              SERIAL      PRIMARY KEY NOT NULL,
    department      VARCHAR(30)             NOT NULL,
);

CREATE OR REPLACE TABLE jobs (
    id              SERIAL      PRIMARY KEY NOT NULL,
    job             VARCHAR(30)             NOT NULL,
);

CREATE OR REPLACE TABLE employees (
    id              SERIAL      PRIMARY KEY NOT NULL,
    name            VARCHAR(30)             NOT NULL,
    datetime        VARCHAR(20)             NOT NULL,
    department_id   INT                     references departments(id),
    job_id          INT                     references jobs(id),
);