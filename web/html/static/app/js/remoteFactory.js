/**
 * Author: Michal Szczepanski
 * Date: 22/11/15
 * Time: 00:10
 */

craftApp.factory('RemoteConnect', ['$http', 'AppModel', function($http, AppModel) {
    var RemoteConnect = {

    }
    return RemoteConnect;
}]);

craftApp.factory('RemoteOld', ['$http', 'AppModel', function($http, AppModel) {

    function checkValid(data) {
        var result = data.code == 0 ? true : false;
        if(data.msg != '') {
            AppModel.flash.add({'type':~~(data.code/100), 'message':data.msg, 'time':data.time});
        }
        return result;
    }
    var RemoteOld = {
        getData: function () {
            $http({
                url: '/data',
                method: 'GET'
            }).success(function(data){
                if(checkValid(data)) {
                    AppModel.dbconf = data.data;
                    var db = data.data.db;
                    for(var i =0;i<db.length;i++) {
                        // DEFAULT DATABASE SET HERE
                        if(db[i].name == 'sqlite') {
                            AppModel.db = db[i];
                            break;
                        }
                    }
                    // assign framework
                    var orm = data.data.orm;
                    for(var i =0;i<orm.length;i++) {
                        if(orm[i].language == 'python') {
                            AppModel.orm = orm[i];
                            AppModel.ormSelected = orm[i].orm[0];
                            AppModel.tabulation = orm[i].tabulation;
                            break;
                        }
                    }
                    AppModel.separator = data.data.separator[0];
                }
            });
        },
        testConnection: function() {
            $http({
                url: '/db/test',
                method: 'POST',
                data: AppModel.db
            }).success(function(data) {
                checkValid(data);
            });
        },
        generateCode: function() {
            out = {
                language:AppModel.orm.language,
                orm:AppModel.ormSelected,
                tabulation:AppModel.tabulation,
                db:AppModel.selectedConnection,
                separator:AppModel.separator,
            }
            $http({
                url: '/code/generate',
                method: 'POST',
                data: out
            }).success(function(data) {
                if(checkValid(data)) {
                    var orm = data.data.orm,
                        code = '';
                    for(var i = 0;i<orm.length;i++) {
                        code += orm[i].data;
                    }
                    AppModel.code = code;
                }
            });
        }
    }
    return RemoteOld;
}]);

craftApp.factory('RemoteCall', ['RemoteOld', 'RemoteConnect',
    function (RemoteOld, RemoteConnect) {
        var RemoteCall = angular.extend({}, RemoteOld);
        RemoteCall = angular.extend(RemoteCall, RemoteConnect);
        return RemoteCall;
    }
]);
