from asyncio import gather, sleep
from pathlib import Path
from typing import Any

from pytest import mark

from lspscript.client import Client, StdIOConnectionParams


async def test_server_capabilities() -> None:
    params = StdIOConnectionParams(
        launch_command="node mock-server/out/index.js --stdio test/test_server_capabilities.json")
    async with Client(params) as client:
        repo_uri = Path(".").resolve().as_uri()

        assert client.check_feature("workspace/didCreateFiles",
                                    file_operations=[repo_uri + "/test/test_capabilities.py",
                                                     repo_uri + "/TEST/test_capabilities.py"])
        assert not client.check_feature("workspace/didCreateFiles",
                                        file_operations=[repo_uri + "/test/test_capabilities.json"])

        assert client.check_feature("textDocument/semanticTokens",
                                    text_documents=[repo_uri + "/test/test_capabilities.py"])
        assert not client.check_feature("textDocument/semanticTokens",
                                        text_documents=[repo_uri + "/test/test_capabilities.py",
                                                        repo_uri + "test_server_capabilities.json"])
        assert client.check_feature("textDocument/semanticTokens", semantic_tokens=["full"])

        assert client.check_feature("textDocument/documentColor")
        assert client.check_feature("textDocument/definition")
        assert client.check_feature("textDocument/hover")
        assert not client.check_feature("textDocument/implementation")


async def run_dynamic_registration(client: Client, method: str, **kwargs: Any) -> None:
    async def schedule_registration() -> None:
        await sleep(0.2)
        await client.send_notification("$/go", None)

    assert not client.check_feature(method, **kwargs)
    # Run the delayed trigger for the registration and require_feature at the same time,
    # so require_feature actually awaits something immediately returning.
    await gather(schedule_registration(), client.require_feature(method, **kwargs))
    assert client.check_feature(method, **kwargs)


@mark.slow
async def test_dynamic_registration() -> None:
    params = StdIOConnectionParams(
        launch_command="node mock-server/out/index.js --stdio test/test_dynamic_registration.json")
    async with Client(params) as client:
        repo_uri = Path(".").resolve().as_uri()

        await run_dynamic_registration(client, "workspace/didCreateFiles",
                                       file_operations=[repo_uri + "/test/test_capabilities.py",
                                                        repo_uri + "/TEST/test_capabilities.py"])
        await run_dynamic_registration(client, "textDocument/semanticTokens",
                                       text_documents=[repo_uri + "/test/test_capabilities.py"],
                                       semantic_tokens=["full"])
        await run_dynamic_registration(client, "textDocument/documentColor")
