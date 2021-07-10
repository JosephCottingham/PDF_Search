CREATE DATABASE pdf; 
\c pdf 
CREATE TABLE pdf (
    id serial PRIMARY KEY,
    url varchar(512),
    title varchar(64)
);

CREATE TABLE keyword (
    id serial PRIMARY KEY,
    word varchar(64)
);

CREATE TABLE pdf_keyword (
  pdf_id int REFERENCES pdf,
  keyword_id int REFERENCES keyword,
  CONSTRAINT pdf_keyword_pkey PRIMARY KEY (pdf_id, keyword_id)
); 