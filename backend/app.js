var createError = require('http-errors');
var express = require('express');
var path = require('path');
var logger = require('morgan');
var cors = require('cors');

var llmRouter = require('./routes/llm');

var app = express();

app.use(cors({
    origin: true,
    credentials: true,
    methods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
    allowedHeaders: ['Content-Type', 'Authorization']
}));

// Disable caching for all requests
app.use((req, res, next) => {
    res.setHeader("Cache-Control", "no-store, no-cache, must-revalidate, proxy-revalidate");
    res.setHeader("Pragma", "no-cache");
    res.setHeader("Expires", "0");
    res.setHeader("Surrogate-Control", "no-store");
    next();
});

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false })); // Add this for form data
app.use(express.static(path.join(__dirname, 'public')));

app.use('/llm', llmRouter);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
    next(createError(404));
});

app.use(function(err, req, res, next) {
  // set locals, only providing error in development
    const errorResponse = {
        error: {
            message: err.message,
            status: err.status || 500
        }
    };

    // Include stack trace only in development
    if (req.app.get('env') === 'development') {
        errorResponse.error.stack = err.stack;
    }

    // Send JSON error response instead of rendering HTML
    res.status(err.status || 500).json(errorResponse);
});

module.exports = app;