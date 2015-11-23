/**
 * Author: Michal Szczepanski
 * Date: 22/11/15
 * Time: 00:10
 */

craftApp.factory('CraftValidator', ['AppModel', function(AppModel){
    var CraftValidator = {
        responseValid: function (data) {
            var result = data.code == 0 ? true : false;
            if(data.msg != '') {
                AppModel.flash.add({'type':~~(data.code/100), 'message':data.msg, 'time':data.time});
            }
            return result;
        }
    }
    return CraftValidator;
}]);

craftApp.factory('RemoteDatabase', ['$http', 'AppModel', 'CraftValidator',
    function($http, AppModel, CraftValidator) {
        var RemoteDatabase = {
            addConnection: function (db) {
                $http({
                    url: '/db/connection/add',
                    method: 'POST',
                    data: db
                }).success(function (data) {
                    CraftValidator.responseValid(data);
                });
                console.log('/db/connection/add');
            },
            removeConnection: function (db) {
                console.log('/db/connection/remove');
                $http({
                    url: '/db/connection/remove',
                    method: 'POST',
                    data: db
                }).success(function (data) {
                    CraftValidator.responseValid(data);
                });
            },
            listConnections: function () {
                $http({
                    url: '/db/connection/list',
                    method: 'GET'
                }).success(function (data) {
                    CraftValidator.responseValid(data);
                    console.log(data);
                    AppModel.databases = data.data;
                    AppModel.selectedConnection = data.data[0];
                });
                console.log('/db/connection/list');
            },
            testConnection: function () {
                $http({
                    url: '/db/connection/test',
                    method: 'POST',
                    data: AppModel.db
                }).success(function (data) {
                    CraftValidator.responseValid(data);
                });
                console.log('/db/connection/test');
            },
            query: function (data) {
                $http({
                    url: '/db/query',
                    method: 'POST',
                    data: data
                }).success(function (data) {
                    CraftValidator.responseValid(data);
                });
                console.log('/db/query');
            },
            dbStructure: function (db) {
                $http({
                    url: '/db/structure/'+db.name,
                    method: 'GET'
                }).success(function (data) {
                    CraftValidator.responseValid(data);
                });
                console.log('/db/structure');
            }
        }
        return RemoteDatabase;
    }
]);

craftApp.factory('RemoteOld', ['$http', 'AppModel', 'CraftValidator',
    function($http, AppModel, CraftValidator) {
        var RemoteOld = {
            getData: function () {
                $http({
                    url: '/data',
                    method: 'GET'
                }).success(function (data) {
                    if (CraftValidator.responseValid(data)) {
                        AppModel.dbconf = data.data;
                        var db = data.data.db;
                        for (var i = 0; i < db.length; i++) {
                            // DEFAULT DATABASE SET HERE
                            if (db[i].name == 'sqlite') {
                                AppModel.db = db[i];
                                break;
                            }
                        }
                        // assign framework
                        var orm = data.data.orm;
                        for (var i = 0; i < orm.length; i++) {
                            if (orm[i].language == 'python') {
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
            generateCode: function () {
                out = {
                    language: AppModel.orm.language,
                    orm: AppModel.ormSelected,
                    tabulation: AppModel.tabulation,
                    db: AppModel.selectedConnection,
                    separator: AppModel.separator,
                }
                $http({
                    url: '/code/generate',
                    method: 'POST',
                    data: out
                }).success(function (data) {
                    if (CraftValidator.responseValid(data)) {
                        var orm = data.data.orm,
                            code = '';
                        for (var i = 0; i < orm.length; i++) {
                            code += orm[i].data;
                        }
                        AppModel.code = code;
                    }
                });
            }
        }
        return RemoteOld;
    }
]);

craftApp.factory('RemoteCall', ['RemoteOld', 'RemoteDatabase',
    function (RemoteOld, RemoteDatabase) {
        var RemoteCall = angular.extend({}, RemoteOld);
        RemoteCall = angular.extend(RemoteCall, RemoteDatabase);
        return RemoteCall;
    }
]);
