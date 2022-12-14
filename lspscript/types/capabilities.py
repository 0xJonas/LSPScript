from typing import List, Optional
from dataclasses import dataclass
from .structures import *


@dataclass
class FeatureRegistration:
    id: Optional[str]
    method: str
    document_selector: Optional[DocumentSelector]
    options: Any


def _capability_to_feature_registration(capability: Any, method: str) -> FeatureRegistration:
    if isinstance(capability, TextDocumentRegistrationOptions):
        document_selector = capability.documentSelector
    else:
        document_selector = None
    if isinstance(capability, StaticRegistrationOptions):
        id = capability.id
    else:
        id = None
    return FeatureRegistration(id, method, document_selector, capability)


def server_capabilities_to_feature_registrations(capabilities: ServerCapabilities) -> List[FeatureRegistration]:
    out: List[FeatureRegistration] = []
    if capabilities and capabilities.implementationProvider not in [None, False]:
        out.append(_capability_to_feature_registration(capabilities.implementationProvider, "textDocument/implementation"))
    if capabilities and capabilities.typeDefinitionProvider not in [None, False]:
        out.append(_capability_to_feature_registration(capabilities.typeDefinitionProvider, "textDocument/typeDefinition"))
    if capabilities and capabilities.colorProvider not in [None, False]:
        out.append(_capability_to_feature_registration(capabilities.colorProvider, "textDocument/documentColor"))
    if capabilities and capabilities.foldingRangeProvider not in [None, False]:
        out.append(_capability_to_feature_registration(capabilities.foldingRangeProvider, "textDocument/foldingRange"))
    if capabilities and capabilities.declarationProvider not in [None, False]:
        out.append(_capability_to_feature_registration(capabilities.declarationProvider, "textDocument/declaration"))
    if capabilities and capabilities.selectionRangeProvider not in [None, False]:
        out.append(_capability_to_feature_registration(capabilities.selectionRangeProvider, "textDocument/selectionRange"))
    if capabilities and capabilities.callHierarchyProvider not in [None, False]:
        out.append(_capability_to_feature_registration(capabilities.callHierarchyProvider, "textDocument/prepareCallHierarchy"))
    if capabilities and capabilities.semanticTokensProvider not in [None, False]:
        out.append(_capability_to_feature_registration(capabilities.semanticTokensProvider, "textDocument/semanticTokens"))
    if capabilities and capabilities.linkedEditingRangeProvider not in [None, False]:
        out.append(_capability_to_feature_registration(capabilities.linkedEditingRangeProvider, "textDocument/linkedEditingRange"))
    if capabilities and capabilities.workspace and capabilities.workspace.get("fileOperations") and capabilities.workspace.get("fileOperations").willCreate not in [None, False]:
        out.append(_capability_to_feature_registration(capabilities.workspace["fileOperations"].willCreate, "workspace/willCreateFiles"))
    if capabilities and capabilities.workspace and capabilities.workspace.get("fileOperations") and capabilities.workspace.get("fileOperations").willRename not in [None, False]:
        out.append(_capability_to_feature_registration(capabilities.workspace["fileOperations"].willRename, "workspace/willRenameFiles"))
    if capabilities and capabilities.workspace and capabilities.workspace.get("fileOperations") and capabilities.workspace.get("fileOperations").willDelete not in [None, False]:
        out.append(_capability_to_feature_registration(capabilities.workspace["fileOperations"].willDelete, "workspace/willDeleteFiles"))
    if capabilities and capabilities.monikerProvider not in [None, False]:
        out.append(_capability_to_feature_registration(capabilities.monikerProvider, "textDocument/moniker"))
    if capabilities and capabilities.typeHierarchyProvider not in [None, False]:
        out.append(_capability_to_feature_registration(capabilities.typeHierarchyProvider, "textDocument/prepareTypeHierarchy"))
    if capabilities and capabilities.inlineValueProvider not in [None, False]:
        out.append(_capability_to_feature_registration(capabilities.inlineValueProvider, "textDocument/inlineValue"))
    if capabilities and capabilities.inlayHintProvider not in [None, False]:
        out.append(_capability_to_feature_registration(capabilities.inlayHintProvider, "textDocument/inlayHint"))
    if capabilities and capabilities.diagnosticProvider not in [None, False]:
        out.append(_capability_to_feature_registration(capabilities.diagnosticProvider, "textDocument/diagnostic"))
    if capabilities and capabilities.completionProvider not in [None, False]:
        out.append(_capability_to_feature_registration(capabilities.completionProvider, "textDocument/completion"))
    if capabilities and capabilities.hoverProvider not in [None, False]:
        out.append(_capability_to_feature_registration(capabilities.hoverProvider, "textDocument/hover"))
    if capabilities and capabilities.signatureHelpProvider not in [None, False]:
        out.append(_capability_to_feature_registration(capabilities.signatureHelpProvider, "textDocument/signatureHelp"))
    if capabilities and capabilities.definitionProvider not in [None, False]:
        out.append(_capability_to_feature_registration(capabilities.definitionProvider, "textDocument/definition"))
    if capabilities and capabilities.referencesProvider not in [None, False]:
        out.append(_capability_to_feature_registration(capabilities.referencesProvider, "textDocument/references"))
    if capabilities and capabilities.documentHighlightProvider not in [None, False]:
        out.append(_capability_to_feature_registration(capabilities.documentHighlightProvider, "textDocument/documentHighlight"))
    if capabilities and capabilities.documentSymbolProvider not in [None, False]:
        out.append(_capability_to_feature_registration(capabilities.documentSymbolProvider, "textDocument/documentSymbol"))
    if capabilities and capabilities.codeActionProvider not in [None, False]:
        out.append(_capability_to_feature_registration(capabilities.codeActionProvider, "textDocument/codeAction"))
    if capabilities and capabilities.workspaceSymbolProvider not in [None, False]:
        out.append(_capability_to_feature_registration(capabilities.workspaceSymbolProvider, "workspace/symbol"))
    if capabilities and capabilities.codeLensProvider not in [None, False]:
        out.append(_capability_to_feature_registration(capabilities.codeLensProvider, "textDocument/codeLens"))
    if capabilities and capabilities.documentLinkProvider not in [None, False]:
        out.append(_capability_to_feature_registration(capabilities.documentLinkProvider, "textDocument/documentLink"))
    if capabilities and capabilities.documentFormattingProvider not in [None, False]:
        out.append(_capability_to_feature_registration(capabilities.documentFormattingProvider, "textDocument/formatting"))
    if capabilities and capabilities.documentRangeFormattingProvider not in [None, False]:
        out.append(_capability_to_feature_registration(capabilities.documentRangeFormattingProvider, "textDocument/rangeFormatting"))
    if capabilities and capabilities.documentOnTypeFormattingProvider not in [None, False]:
        out.append(_capability_to_feature_registration(capabilities.documentOnTypeFormattingProvider, "textDocument/onTypeFormatting"))
    if capabilities and capabilities.renameProvider not in [None, False]:
        out.append(_capability_to_feature_registration(capabilities.renameProvider, "textDocument/rename"))
    if capabilities and capabilities.executeCommandProvider not in [None, False]:
        out.append(_capability_to_feature_registration(capabilities.executeCommandProvider, "workspace/executeCommand"))
    if capabilities and capabilities.workspace and capabilities.workspace.get("fileOperations") and capabilities.workspace.get("fileOperations").didCreate not in [None, False]:
        out.append(_capability_to_feature_registration(capabilities.workspace["fileOperations"].didCreate, "workspace/didCreateFiles"))
    if capabilities and capabilities.workspace and capabilities.workspace.get("fileOperations") and capabilities.workspace.get("fileOperations").didRename not in [None, False]:
        out.append(_capability_to_feature_registration(capabilities.workspace["fileOperations"].didRename, "workspace/didRenameFiles"))
    if capabilities and capabilities.workspace and capabilities.workspace.get("fileOperations") and capabilities.workspace.get("fileOperations").didDelete not in [None, False]:
        out.append(_capability_to_feature_registration(capabilities.workspace["fileOperations"].didDelete, "workspace/didDeleteFiles"))
    if capabilities and capabilities.notebookDocumentSync not in [None, False]:
        out.append(_capability_to_feature_registration(capabilities.notebookDocumentSync, "notebookDocument/sync"))
    return out


_method_to_options_mapping = {
    "textDocument/implementation": ImplementationRegistrationOptions,
    "textDocument/typeDefinition": TypeDefinitionRegistrationOptions,
    "textDocument/documentColor": DocumentColorRegistrationOptions,
    "textDocument/foldingRange": FoldingRangeRegistrationOptions,
    "textDocument/declaration": DeclarationRegistrationOptions,
    "textDocument/selectionRange": SelectionRangeRegistrationOptions,
    "textDocument/prepareCallHierarchy": CallHierarchyRegistrationOptions,
    "textDocument/semanticTokens": SemanticTokensRegistrationOptions,
    "textDocument/linkedEditingRange": LinkedEditingRangeRegistrationOptions,
    "workspace/willCreateFiles": FileOperationRegistrationOptions,
    "workspace/willRenameFiles": FileOperationRegistrationOptions,
    "workspace/willDeleteFiles": FileOperationRegistrationOptions,
    "textDocument/moniker": MonikerRegistrationOptions,
    "textDocument/prepareTypeHierarchy": TypeHierarchyRegistrationOptions,
    "textDocument/inlineValue": InlineValueRegistrationOptions,
    "textDocument/inlayHint": InlayHintRegistrationOptions,
    "textDocument/diagnostic": DiagnosticRegistrationOptions,
    "textDocument/willSaveWaitUntil": TextDocumentRegistrationOptions,
    "textDocument/completion": CompletionRegistrationOptions,
    "textDocument/hover": HoverRegistrationOptions,
    "textDocument/signatureHelp": SignatureHelpRegistrationOptions,
    "textDocument/definition": DefinitionRegistrationOptions,
    "textDocument/references": ReferenceRegistrationOptions,
    "textDocument/documentHighlight": DocumentHighlightRegistrationOptions,
    "textDocument/documentSymbol": DocumentSymbolRegistrationOptions,
    "textDocument/codeAction": CodeActionRegistrationOptions,
    "workspace/symbol": WorkspaceSymbolRegistrationOptions,
    "textDocument/codeLens": CodeLensRegistrationOptions,
    "textDocument/documentLink": DocumentLinkRegistrationOptions,
    "textDocument/formatting": DocumentFormattingRegistrationOptions,
    "textDocument/rangeFormatting": DocumentRangeFormattingRegistrationOptions,
    "textDocument/onTypeFormatting": DocumentOnTypeFormattingRegistrationOptions,
    "textDocument/rename": RenameRegistrationOptions,
    "workspace/executeCommand": ExecuteCommandRegistrationOptions,
    "workspace/didCreateFiles": FileOperationRegistrationOptions,
    "workspace/didRenameFiles": FileOperationRegistrationOptions,
    "workspace/didDeleteFiles": FileOperationRegistrationOptions,
    "workspace/didChangeConfiguration": DidChangeConfigurationRegistrationOptions,
    "textDocument/didOpen": TextDocumentRegistrationOptions,
    "textDocument/didChange": TextDocumentChangeRegistrationOptions,
    "textDocument/didClose": TextDocumentRegistrationOptions,
    "textDocument/didSave": TextDocumentSaveRegistrationOptions,
    "textDocument/willSave": TextDocumentRegistrationOptions,
    "workspace/didChangeWatchedFiles": DidChangeWatchedFilesRegistrationOptions
}


def registration_to_feature_registration(registration: Registration) -> FeatureRegistration:
    cls = _method_to_options_mapping[registration.method]
    options = cls.from_json(registration.registerOptions)
    if isinstance(options, TextDocumentRegistrationOptions):
        document_selector = options.documentSelector
    else:
        document_selector = None
    if isinstance(options, StaticRegistrationOptions):
        id = options.id
    else:
        id = registration.id
    return FeatureRegistration(id, registration.method, document_selector, options)