module.exports = ({ env }) => ({
  auth: {
    secret: env('ADMIN_JWT_SECRET', 'de7b14f79177dbd5e686c63063b9a4d8'),
  },
});
