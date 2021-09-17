## Vue.js Development Notes

This describes the method and tooling used to incorporate [Vue.js](https://vuejs.org)
components into your Django templates. The overall strategy taken is based on [this](https://medium.com/js-dojo/vue-django-best-of-both-frontends-701307871478) series of articles.

### Dependencies

- Ensure that your version of ``django-webpack-loader`` in ``requirements.txt`` is ``~=0.6.0``.
- Ensure that your version of ``webpack-bundle-tracker`` in ``package.json`` is ``^0.4.3``.

### Step-by-Step
1. Create a Vue.js application in your Django project.
   ```vue create vue```

2. Install `webpack-bundle-tracker` into your Vue.js application.
   ```npm install --save-dev webpack-bundle-tracker@^0.4.3```
   
3. Add the `vue.config.js` configuration file to your Vue.js application

4. Add your components (`.vue`) and entry points (i.e. `main.js`) files. In this demonstration:
    - `vue/src/components/{App, App02}.vue`, and
    - `vue/src/components/{main, main_02}.js` were added.

5. Add `django-webpack-loader` to your TOM Toolkit project.
    - `requirements.txt` needs updating
    - `INSTALLED_APPS` in your `settings.py` needs `webpack_loader`.

6. Configure `django-webpack-loader` in your `settings.py`.
    - add `VUE_FRONTEND_DIR`, which is used by
    - add `WEBPACK_LOADER` dictionary.
    
7. Add the Django URLs and templates that will incorporate you Vue.js components.
    - in this case `vue_health_check_{01, 02}.html` were added,
    - add URLs to `tom_demo_base/urls.py`
    
8. For deployment, update the `Dockerfile` to
    - install `nvm`, `node`, and `npm`
    - run `npm install` to install the `node_modules`, and
    - run `npm run build` to place your JS and CSS files in your `STATIC_DIRS`.
    
## How it Works
Key things to note:
- in `vue.config.js`, your `pages` dictionary defines every component that will be served.
  - the dictionary key defines the `render_bundle` names that will be used in your template `.html` flie
  - the value `entry` key is the file name of the entrypoint `.js` file.

- One the Vue.js side, `webpack-bundle-tracker` writes the `webpack-stats.json` file upon `npm run build` (for production) or `npm run server` (for development).
- On the Django side, `webpack-stats.json` is read by `django-webpack-loader`

- the Vue component entry points (i.e. `vue/src/components/main.js`)
  - instantiate a Vue app (`new Vue` or `createApp()`) for each Vue component, and
  - associate that Vue component with an html element id.
    
- the Django html templates refer to the element id from the entrypoint:
  - `<div id="id-from-entrypoint">`
    
- the content of the `<div>` refers the Vue component associated with the element.
