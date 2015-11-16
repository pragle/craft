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

            conf.testConnectionClick = function() {
                RemoteCall.testConnection();
            }

            conf.ormSelectedChange = function() {
                AppModel.ormSelected = AppModel.orm.orm[0];
                AppModel.tabulation = AppModel.orm.tabulation;
            }

            conf.generateClick = function() {
                RemoteCall.generateCode();
            }
        }]);
})();