'use strict';

/**
 * job-carrier service.
 */

const { createCoreService } = require('@strapi/strapi').factories;

module.exports = createCoreService('api::job-carrier.job-carrier');
