import express from 'express';
import cors from 'cors';
import bodyParser from 'body-parser';
require('dotenv').config();

export const app = express()

app.use(bodyParser.json({limit: "50mb"}));
app.use(bodyParser.urlencoded({limit: "50mb", extended: true, parameterLimit:50000}));

let corsOptions;

if (process.env.NODE_ENV === 'development') {
  corsOptions = {
    origin: "*"
  }
} else {
  corsOptions = {
    origin: "*"
  }
} 

app.use(cors(corsOptions));
