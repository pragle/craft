/**
 * Author: Michal Szczepanski
 * Date: 07/11/15
 * Time: 15:53
 */

(function () {
    angular.module('mainModule', [])
        .config([function () {
            console.log("mainModule configuration");
        }])
        .run([function () {
            console.log("mainModule run")
        }])
        .controller('MainCtrl', ['$scope', 'AppModel', function ($scope, AppModel) {
            var main = this;

            main.data = AppModel;
        }])
        .controller('PopupCtrl', ['$scope', 'AppModel', 'RemoteCall', function ($scope, AppModel, RemoteCall) {
            var popup = this;

            popup.testConnectionClick = function() {
                RemoteCall.testConnection();
            }

            popup.ormSelectedChange = function() {
                AppModel.ormSelected = AppModel.orm.orm[0];
                AppModel.tabulation = AppModel.orm.tabulation;
            }

            popup.generateCode = function() {
                RemoteCall.generateCode();
            }

            popup.addConnection = function() {
                var db = angular.copy(AppModel.db);
                AppModel.selectedConnection = db;
                AppModel.databases.push(db);
                console.log('add connection');
            }
        }])
})();