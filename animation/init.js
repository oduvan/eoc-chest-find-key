requirejs(['ext_editor_io', 'jquery_190'],
    function (extIO, $) {
        
        var io = new extIO({
            multipleArguments: true,
            functions: {
                python: 'find_key',
                js: 'findKey'
            }
        });
        io.start();
    }
);
