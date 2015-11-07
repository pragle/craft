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
        }]);
})();