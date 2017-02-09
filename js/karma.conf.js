module.exports = function (config) {
    config.set({
        basePath: '',
        frameworks: ['jasmine'],
        files: [
            'specs.js'
        ],
        exclude: [],
        preprocessors: {
            'specs.js': ['webpack']
        },
        reporters: ['spec'],
        port: 9876,
        colors: true,
        logLevel: config.LOG_INFO,
        autoWatch: true,
        browsers: ['PhantomJS'],
        singleRun: false,
        concurrency: Infinity,
        webpack: require('./webpack.make')('test')
    })
};
