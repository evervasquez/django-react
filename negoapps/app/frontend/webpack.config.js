const path = require('path');

module.exports = {
    entry: {
        index: path.resolve(__dirname, './src/index.js'),
        //contact: path.resolve(__dirname, 'src/js/contact.js')
    },
    output: {
        path: path.resolve(__dirname, './static/frontend'),
        filename: 'main.js'
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: "babel-loader"
                }
            }, {
                test: /\.css$/,
                use: ['style-loader', 'css-loader']
            }
        ]
    },
    resolve: {
     extensions: ['.js']
   }
};
