webpackJsonp([2],{126:function(e,t,a){"use strict";function o(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}function l(e,t){if(!e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return!t||"object"!==typeof t&&"function"!==typeof t?e:t}function r(e,t){if("function"!==typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function, not "+typeof t);e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,enumerable:!1,writable:!0,configurable:!0}}),t&&(Object.setPrototypeOf?Object.setPrototypeOf(e,t):e.__proto__=t)}Object.defineProperty(t,"__esModule",{value:!0});var n=function(){function e(e,t){for(var a=0;a<t.length;a++){var o=t[a];o.enumerable=o.enumerable||!1,o.configurable=!0,"value"in o&&(o.writable=!0),Object.defineProperty(e,o.key,o)}}return function(t,a,o){return a&&e(t.prototype,a),o&&e(t,o),t}}(),i=a(0),c=function(e){return e&&e.__esModule?e:{default:e}}(i),s=a(22);a(133);var f=window.$,m=function(e){function t(){return o(this,t),l(this,(t.__proto__||Object.getPrototypeOf(t)).apply(this,arguments))}return r(t,e),n(t,[{key:"componentDidMount",value:function(){f(".portfolio-item").magnificPopup({type:"inline",preloader:!1,focus:"#username",modal:!0}),f(document).on("click",".portfolio-modal-dismiss",function(e){f.magnificPopup.close()})}},{key:"render",value:function(){var e=this.props.data.module,t=e.portfolio_items.map(function(e,t){return c.default.createElement("div",{key:t,className:"col-md-6 col-lg-4"},c.default.createElement("a",{className:"portfolio-item d-block mx-auto",href:"#portfolio-modal-"+t},c.default.createElement("div",{className:"portfolio-item-caption d-flex position-absolute h-100 w-100"},c.default.createElement("div",{className:"portfolio-item-caption-content my-auto w-100 text-center text-white"},c.default.createElement("i",{className:"fa fa-search-plus fa-3x"}))),c.default.createElement("img",{className:"img-fluid",src:e.image.file,alt:""})))}),a=e.portfolio_items.map(function(e,t){var a=e.link?e.link.url:"";return c.default.createElement("div",{key:t,className:"portfolio-modal mfp-hide",id:"portfolio-modal-"+t},c.default.createElement("div",{className:"portfolio-modal-dialog bg-white"},c.default.createElement("a",{className:"close-button d-none d-md-block portfolio-modal-dismiss",href:"#"},c.default.createElement("i",{className:"fa fa-3x fa-times"})),c.default.createElement("div",{className:"container text-center"},c.default.createElement("div",{className:"row"},c.default.createElement("div",{className:"col-lg-8 mx-auto"},c.default.createElement("h2",{className:"text-secondary text-uppercase mb-0"},e.portfolio.title),c.default.createElement("hr",{className:"star-dark mb-5"}),c.default.createElement("img",{className:"img-fluid mb-5",src:e.image.file,alt:""}),c.default.createElement("p",{className:"mb-5"},e.text),c.default.createElement(s.NavLink,{className:"btn btn-primary btn-lg rounded-pill portfolio-modal-dismiss mr-2",to:a},c.default.createElement("i",{className:"fa fa-external-link mr-2"}),"Details"),c.default.createElement("a",{className:"btn btn-primary btn-lg rounded-pill portfolio-modal-dismiss",href:"#"},c.default.createElement("i",{className:"fa fa-close mr-2"}),"Close"))))))});return c.default.createElement("div",{className:"bg-white"},c.default.createElement("section",{className:"portfolio ",id:"portfolio"},c.default.createElement("div",{className:"container"},c.default.createElement("h2",{className:"text-center text-uppercase text-secondary mb-0"},"Portfolio"),c.default.createElement("hr",{className:"star-dark mb-5"}),c.default.createElement("div",{className:"row"},t))),a)}}]),t}(c.default.Component);t.default=m},133:function(e,t,a){var o=a(134);"string"===typeof o&&(o=[[e.i,o,""]]);var l={hmr:!1};l.transform=void 0;a(123)(o,l);o.locals&&(e.exports=o.locals)},134:function(e,t,a){t=e.exports=a(122)(!0),t.push([e.i,"bg-white{background:#fff}","",{version:3,sources:["/app/src/client/src/style/Portfolio.css"],names:[],mappings:"AAAA,SACI,eAAmB,CACtB",file:"Portfolio.css",sourcesContent:["bg-white{\n    background:#ffffff;\n}\n"],sourceRoot:""}])}});
//# sourceMappingURL=2.8b706051.chunk.js.map