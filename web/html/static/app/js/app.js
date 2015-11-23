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

var craftApp = angular.module('craftApp',
    ['ui.router', 'mainModule', 'dbModule', 'testModule'])
    .config(['$stateProvider', '$urlRouterProvider', function ($stateProvider, $urlRouterProvider) {
        console.log("Config");
        $urlRouterProvider.otherwise('/test');

        $stateProvider.state('test', {
            url: '/test',
            templateUrl: '/static/html/view/test.html',
            controller: 'TestCtrl as test'
        }).state('database', {
            url: '/database',
            templateUrl: '/static/html/view/db.html',
            controller:'DatabaseCtrl as db'
        })
    }])
    .run(['RemoteCall', function (RemoteCall) {
        console.log("Run");
        RemoteCall.getData();
        RemoteCall.listConnections();
    }]);

craftApp.factory('AppModel', ['$timeout', function ($timeout) {
    var AppModel = {
        databases:[],
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

craftApp.directive('popupReady', function() {
    return {
        restrict: 'A',
        link: function($scope, elem, attrs) {
            elem.ready(function(){
                console.log(attrs);
                $('#'+attrs.id).modal('show');
            })
        }
    }
})