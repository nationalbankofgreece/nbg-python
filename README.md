# NBG API Python Library

Python library for the NBG API with a Django front-end, to perform API calls through the browser.

More information on the NBG API can be found at https://nbgdemo.portal.azure-api.net.

## Configuration

To configure the NBG API Python client create a file with `.env` as its name in the root directory of your project. Add your subscription primary and secondary keys in the following format in this file:

```
NBG_PRIMARY_KEY=your_primary_key_here
NBG_SECONDARY_KEY=your_secondary_key_here
```

## Usage

First of all, in order to use `nbg` open a Python terminal and import it like this:

```python
import nbg
```

Below you can find several examples on how to use the NBG API with the `nbg` library.

### Creating a resource

```python
data = {
    'vehicleType': 'train',
    'maxSpeed': 125,
    'avgSpeed': 90,
    'speedUnit': 'mph'
}
response = nbg.create_resource(data)
```

### Modifying a resource

```python
data = {
    'id': 1
}
response = nbg.modify_resource(data)
```

### Removing a resource

```python
data = {
    'id': 1
}
response = nbg.remove_resource(data)
```

### Retrieve resource headers

```python
data = {
    'id': 1
}
response = nbg.retrieve_resource_headers(data)
```

### Retrieve a resource

```python
data = {
    'param1': 'sample'
    'param2': '{number}'
}
response = nbg.retrieve_resource(data)
```

### Retrieve a cached resource

```python
data = {
    'param1': 'sample'
    'param2': '{number}'
}
response = nbg.retrieve_resource_cached(data)
```

## License

This boilerplate is licensed under the MIT License.
