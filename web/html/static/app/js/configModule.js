/**
 * Author: Michal Szczepanski
 * Date: 07/11/15
 * Time: 16:36
 */

(function () {
    angular.module('configModule', [])
        .config([function () {
            console.log("configModule configuration");
        }])
        .run([function () {
            console.log("configModule run")
        }])
        .controller('ConfigCtrl', ['$scope', 'RemoteCall', 'AppModel', function ($scope, RemoteCall, AppModel) {
            var conf = this;

            conf.siema = 'siema';

            conf.testConnectionClick = function() {
                RemoteCall.testConnection();
            }

            var i = 0;

            conf.flashTest = function() {
                i += 1;
                var time = ~~(Math.random()*10000);
                var type = ~~(Math.random()*(AppModel.flash.types.length-1));
                // success, danger
                console.log(type);
                console.log("type : "+AppModel.flash.types[type]+" time : "+time);
                AppModel.flash.add({'type':AppModel.flash.types[type],'message':'Test '+i, 'time':time})
            }
        }]);
})();