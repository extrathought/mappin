# Mapping Tweets

## Prerequisites

- Twitter Developer account: if you don’t have one already, you can [apply for one](https://developer.twitter.com/en/apply-for-access.html).
- A Twitter developer app, which can be created in your Twitter developer account.
- A bearer token from your app in the [Twitter developer portal](https://developer.twitter.com/en/docs/developer-portal/overview)
- Set up a project to obtain access to v2 endpoints in the [Twitter developer portal](https://developer.twitter.com/en/docs/developer-portal/overview)l
- Access to the [filtered stream](http://developer.twitter.com/en/docs/twitter-api/tweets/filter-stream) endpoint. You will also need to activate it in the [Twitter developer portal](https://developer.twitter.com/en/docs/developer-portal/overview) dashboard within your Twitter Developer account.
- [Node.js](https://nodejs.org/)
- [Npm](https://docs.npmjs.com/about-npm) (This is automatically installed with Node. Make sure you have npm 5.2 or higher.)
- [Npx](https://www.npmjs.com/package/npx) (Included with npm 5.2 or higher)

## Install

```sh
npm install
```

## Environment setup

- Your bearer token can be found from your app in the [Twitter developer portal](https://developer.twitter.com/en/docs/developer-portal/overview)

```sh
export TWITTER_BEARER_TOKEN=<REPLACE WITH YOUR BEARER TOKEN INCLUDING ANGLE BRACKETS>
```

## Usage

```sh
npm start
```


# How to Contribute

We'd love to get patches from you!

## 📝 License

By contributing your code, you agree to license your contribution under the
terms of the APLv2: https://github.com/twitter/repo-scaffolding/blob/master/LICENSE

## Code of Conduct

Read our [Code of Conduct](CODE_OF_CONDUCT.md) for the project.
