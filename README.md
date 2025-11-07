
The project is a fully typed package for retrieving environment variables in python. Main use case is for when writing a microservice or job, I always write the same boilerplate code for loading environment variables and then checking that they have been set and are the right types. Other packages exist that operate similarly, but often come bundled with features that I don't want or need. The package provides 4 functions (env_str, env_int, env_bool, env_float) and each function works in the same way and takes the same arguments, but just returns a differnt type. This package has no external dependencies

This is something I do in every project I work on and it should reduce boilerplate. No more 

### todo before publishing on pypi
- rename to getenv_str, getenv_int, etc to better suit os lib
- Implement & test of env_float
- implement & test getenv_enum
- Write clear docstrings and comments as required
- Write good readme
- git cicd pipeline
- provide example usage
- Get 100% code test coverage