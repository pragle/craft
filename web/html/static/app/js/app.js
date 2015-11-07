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
        console.log("Config")
        $urlRouterProvider.otherwise('/home')

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
    var RemoteCall = {
        getData: function () {
            $http({
                url: '/data',
                method: 'GET'
            }).success(function(data){
                AppModel.data = data.data;
                var db = data.data.db;
                for(var i =0;i<db.length;i++) {
                    // DEFAULT DATABASE SET HERE
                    if(db[i].name == 'sqlite') {
                        AppModel.db = db[i];
                        break;
                    }
                }
            })
        },
        testConnection: function() {
            $http({
                url: '/connection/test',
                method: 'POST',
                data:AppModel.db
            }).success(function(data) {
                AppModel.connectionTest = data.code == 0;
            });
        }
    }
    return RemoteCall;
}]);

craftApp.factory('AppModel', ['$timeout', function ($timeout) {
    var AppModel = {
        flash: {
            messages:[],
            types:['success', 'info', 'warning', 'danger'],
            add: function(message) {
                var i = AppModel.flash.messages.length+1;
                message.id = i;
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