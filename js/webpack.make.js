var path = require('path');

module.exports = function make(env) {
    return {
        entry: getEntry(env),
        ouput: {
            path: path.join(__dirname, 'dist'),
            filename: 'js/[name].js',
            sourceMapFilename: '[file].map'
        },
        resolve: {
            extensions: ['', '.js']
        },
        module: {
            loaders: [
                {
                    test: /\.js$/,
                    loader: 'babel',
                    exclude: /node_modules/,
                    query: {
                        presets: ['es2015']
                    }
                }
            ]
        }
    }
};

function getEntry(env) {
    if (env === 'test')
        return undefined;

    return env === 'test'
        ? undefined
        : 'game-of-life.js'
}