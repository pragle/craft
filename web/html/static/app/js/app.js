/*
 *
 * Copyright (c) 2015-2015, Michal Szczepanski
 * All rights reserved.
 *
 * This source code is licensed under the BSD-style license found in the
 * LICENSE file in the root directory of this source tree.
 *
 */

/**
 * Author: Michal Szczepanski
 * Date: 06/11/15
 * Time: 23:04
 */

var craftApp = angular.module('craftApp', ['ui.router', 'mainModule', 'configModule'])
    .config(['$stateProvider', '$urlRouterProvider', function ($stateProvider, $urlRouterProvider) {
        console.log("Config");
        $urlRouterProvider.otherwise('/home');

        $stateProvider.state('home', {
            url: '/home',
            templateUrl: '/static/html/view/home.html'
        }).state('configuration', {
            url: '/configuration',
            templateUrl: '/static/html/view/configuration.html',
            controller:'ConfigCtrl as conf'
        })
    }])
    .run(['RemoteCall', function (RemoteCall) {
        console.log("Run");
        RemoteCall.getData();
    }]);

craftApp.factory('RemoteCall', ['$http', 'AppModel', function ($http, AppModel) {
    function checkValid(data) {
        var result = data.code == 0 ? true : false;
        if(data.msg != '') {
            AppModel.flash.add({'type':~~(data.code/100), 'message':data.msg, 'time':data.time});
        }
        return result;
    }
    var RemoteCall = {
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
                    var fram = data.data.framework;
                    for(var i =0;i<fram.length;i++) {
                        if(fram[i].language == 'python') {
                            AppModel.framework = fram[i];
                            AppModel.frameworkSelected = fram[i].framework[0];
                            AppModel.tabulation = fram[i].tabulation;
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
                language:AppModel.framework.language,
                framework:AppModel.frameworkSelected,
                tabulation:AppModel.tabulation,
                db:AppModel.db,
                separator:AppModel.separator,
            }
            $http({
                url: '/code/generate',
                method: 'POST',
                data: out
            }).success(function(data) {
                if(checkValid(data)) {
                    console.log(data.data);
                }
            });
        }
    }
    return RemoteCall;
}]);

craftApp.factory('AppModel', ['$timeout', function ($timeout) {
    var AppModel = {
        flash: {
            messages:[],
            id:0,
            types:['success', 'info', 'warning', 'danger'],
            add: function(message) {
                AppModel.flash.id+=1;
                message.id = AppModel.flash.id;
                message.type = AppModel.flash.types[message.type];
                AppModel.flash.messages.push(message);
                $timeout(function() {
                    $(".flash-"+message.id).fadeTo(500, 0).slideUp(500, function(){
                        $(this).remove();
                    });
                }, message.time);
            }
        }
    }

    return AppModel;
}]);