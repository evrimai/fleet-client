# Health

Methods:

- <code title="get /health/">client.health.<a href="./src/fleet/resources/health.py">check</a>() -> object</code>

# Browsers

Types:

```python
from fleet.types import VisitRequest
```

# Scrape

Types:

```python
from fleet.types import BrowserSelectionStrategy
```

## Async

Types:

```python
from fleet.types.scrape import JobStatus
```

## BrowserStrategy

Types:

```python
from fleet.types.scrape import BrowserStrategyResponse
```

# Workflows

Types:

```python
from fleet.types import WorkflowDescribeResponse, WorkflowGetResultsResponse
```

Methods:

- <code title="get /workflows/describe/{workflow_id}">client.workflows.<a href="./src/fleet/resources/workflows/workflows.py">describe</a>(workflow_id) -> <a href="./src/fleet/types/workflow_describe_response.py">WorkflowDescribeResponse</a></code>
- <code title="get /workflows/results/{workflow_id}">client.workflows.<a href="./src/fleet/resources/workflows/workflows.py">get_results</a>(workflow_id) -> <a href="./src/fleet/types/workflow_get_results_response.py">WorkflowGetResultsResponse</a></code>

## Request

Types:

```python
from fleet.types.workflows import RequestCreateResponse
```

Methods:

- <code title="post /workflows/request/scrape">client.workflows.request.<a href="./src/fleet/resources/workflows/request.py">create</a>(\*\*<a href="src/fleet/types/workflows/request_create_params.py">params</a>) -> <a href="./src/fleet/types/workflows/request_create_response.py">RequestCreateResponse</a></code>
